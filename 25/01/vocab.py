#!/usr/bin/env python3
import argparse
import random
import re
from dataclasses import dataclass
from pathlib import Path

LINE_RE = re.compile(r"^(\d+)\.\s(.*)$")
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


@dataclass(frozen=True)
class Vocab:
    word: str
    translation: str
    example: str = ""


def die(msg: str) -> None:
    raise SystemExit(f"{RED}错误:{RESET} {msg}")


def parse_db(path: Path) -> list[Vocab]:
    if not path.exists():
        die(f"文件不存在: {path}")
    seen: set[Vocab] = set()
    order: list[Vocab] = []
    text = path.read_text(encoding="utf-8")
    for i, raw in enumerate(text.splitlines(), 1):
        m = LINE_RE.match(raw)
        if not m:
            continue
        body = m.group(2).strip()
        c = body.count(":")
        if c not in (1, 2):
            die(f"第{i}行不符合规范: {raw}")
        parts = [x.strip() for x in body.split(":")]
        if c == 1:
            word, translation = parts
            example = ""
        else:
            word, translation, example = parts
        if not word or not translation:
            die(f"第{i}行不符合规范: {raw}")
        v = Vocab(word, translation, example)
        if v not in seen:
            seen.add(v)
            order.append(v)
    if len(order) < 4:
        die("有效词条不足 4 条")
    if len({x.translation for x in order}) < 4:
        die("translation 去重后不足 4 条")
    return order


def clear() -> None:
    print("\033[2J\033[H", end="")


def render_question(prompt: str, example: str, options: list[str], correct: int) -> None:
    print(f"{CYAN}{BOLD}词汇练习{RESET}  (Ctrl+C 退出)  累计答对: {GREEN}{correct}{RESET}")
    ex = example if example else "-"
    print(f"\n{BOLD}{prompt}{RESET}: {YELLOW}{ex}{RESET}\n\n")
    for idx, opt in enumerate(options, 1):
        print(f"  {idx}. {opt}")


def pick_vocab(items: list[Vocab], zh_to_en: bool) -> Vocab:
    """全中（中文题干）时：总量≥72 则文件顺序前 36 条与共余条目各占 50% 权重；否则均匀。"""
    n = len(items)
    if not zh_to_en or n < 72:
        return random.choice(items)
    rest = n - 36
    weights = [50.0 / 36] * 36 + [50.0 / rest] * rest
    return random.choices(items, weights=weights, k=1)[0]


def make_round(v: Vocab, items: list[Vocab], zh_to_en: bool) -> tuple[str, str, list[str], str]:
    if zh_to_en:
        prompt = v.translation
        example = ""
        answer = v.word
        wrong_pool = [x.word for x in items if x.word != v.word]
    else:
        prompt = v.word
        example = v.example
        answer = v.translation
        wrong_pool = [x.translation for x in items if x.translation != v.translation]
    options = random.sample(wrong_pool, 3) + [answer]
    random.shuffle(options)
    return prompt, example, options, answer


def quiz(db: list[Vocab]) -> None:
    items = db
    correct = 0
    clear()
    while True:
        zh_to_en = random.random() < 0.5
        v = pick_vocab(items, zh_to_en)
        prompt, example, options, answer = make_round(v, items, zh_to_en)
        ans = options.index(answer) + 1
        while True:
            render_question(prompt, example, options, correct)
            pick = input("\n你的选择(1-4): ").strip()
            if pick not in {"1", "2", "3", "4"}:
                clear()
                print(f"{RED}请输入 1/2/3/4{RESET}\n")
                continue
            break
        if int(pick) == ans:
            correct += 1
            clear()
            print(f"{GREEN}{v.word}: {v.translation}: {v.example}{RESET}\n")
            continue
        print(f"\n{RED}{v.word}: {ans}. {v.translation}: {v.example}{RESET}")
        input("回车继续...")
        clear()


def main() -> None:
    p = argparse.ArgumentParser(description="词汇四选一")
    p.add_argument("path", help="文本文件路径")
    args = p.parse_args()
    db = parse_db(Path(args.path))
    try:
        quiz(db)
    except KeyboardInterrupt:
        print("\n已退出")


if __name__ == "__main__":
    main()
