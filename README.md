# CrackStation, a Decrypter implementation

Cracks one-character, two-character and three-character passwords.

## Overview

This library is a crackstation using sha1 and sha256, which be able to crack any password that is up to three characters in length.In this package, there is a file named v3.py to generate the hash and store the dictionary in data.json. After you import the package named "CrackStation", you can use unit tests in "CrackStationTests" to check if the password is cracked.

## Mission Statement

This library is mainly provided for users who are interested in password cracking for testing and research, not for stealing other people's privacy.

## Installation

### Swift Package Manager

The [Swift Package Manager](https://www.swift.org/package-manager) is "a tool for managing the distribution of Swift code. It's integrated with the Swift build system to automate the process of downloading, compiling, and linking dependencies."

Once you have your Swift package set up, add CrackStation to the list of dependencies in your `Package.swift` file.

```
dependencies: [
        .package(url: "git@github.com:wangsyyy/CrackStation.git", from: "1.1.0")
]
```

## Usage

### The API

`init` for creating a decrypter; `decrypt` for decrypting hashes back to plain-text passwords.

### An example

## Auther

Syu-Wun Wang
