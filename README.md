# AWS Training Code Examples

This repository contains Python code examples used in AWS training courses, demonstrating both AWS service interactions and general utility functions.

## Table of Contents
- [AWS S3 Examples](#aws-s3-examples)
- [Utility Scripts](#utility-scripts)

## AWS S3 Examples

### S3 Bucket Creation and Deletion (s3CreateDelBucket.py)
Creates an S3 bucket and optionally deletes it after creation.

Usage:
```bash
 s3CreateDelBucket.py <bucket_name> <aws_region> [--keep_bucket]
```

### S3 Object Retrieval (s3getobj.py)
Demonstrates how to retrieve an object from an S3 bucket using the AWS SDK for Python (Boto3).

Usage:
```bash
 # Edit bucket_name and object_key variables in the script
 python s3getobj.py
```

### S3 Bucket Existence Check (Demo_S3_HeadBucket_python.py)
Checks if a specified S3 bucket exists and handles various access scenarios.

Usage:
```bash
 # Edit bucket_name variable in the script
 python Demo_S3_HeadBucket_python.py
```

## Utility Scripts

### Temperature Converter (convertTemp.py)
Converts temperatures between Celsius and Fahrenheit.

Usage:
```bash
 python convertTemp.py
 # Then follow the prompts to enter a temperature (e.g., 22C or 72F)
```

### Hello World with Addition (hello2.py)
Simple demonstration of command-line argument processing and basic arithmetic.

Usage:
```bash
 hello2.py <number1> <number2>
```