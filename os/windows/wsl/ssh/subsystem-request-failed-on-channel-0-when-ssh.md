- reliability: "20% (author)"
- date: 2025-01-04
- os: "Darwin floriandeMacBook-Air.local 23.5.0 Darwin Kernel Version 23.5.0: Wed May  1 20:16:51 PDT 2024; root:xnu-10063.121.3~5/RELEASE_ARM64_T8103 arm64"
- author: "Julyfun MacOS14.5 M1"
- assume-you-know: [computer]

# subsystem request failed on channel 0 when ssh

- https://stackoverflow.com/questions/74311661/subsystem-request-failed-on-channel-0-scp-connection-closed
- `ssh -rO` worked for me.
