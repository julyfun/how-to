struct Stu {
    age: i32,
    name: String,
    gpa: f32,
}

fn main() {
    let stu = vec![
        Stu {
            age: 20,
            name: "Alice".to_string(),
            gpa: 3.5,
        },
        Stu {
            age: 21,
            name: "Bob".to_string(),
            gpa: 3.6,
        },
        Stu {
            age: 22,
            name: "Charlie".to_string(),
            gpa: 3.7,
        },
        Stu {
            age: 22,
            name: "Charlie".to_string(),
            gpa: 3.4,
        },
    ];
    let sum: f32 = stu
        .iter()
        .filter(|s| s.gpa >= 3.5 && s.age >= 21 && s.age <= 25)
        .map(|s| s.gpa)
        .sum();
    println!("Sum of GPA: {}", sum);
}

