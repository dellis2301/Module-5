# Module-5

# OWASP Top 10 Secure Coding Assignment

This project demonstrates common vulnerabilities from the OWASP Top 10 and how to properly fix them using secure coding practices. Each section includes a vulnerable example, an explanation of the issue, a secure version of the code, and how the fix improves security.

# 1. Broken Access Control
Vulnerability Explanation

The application allows users to access data by directly supplying a user ID in the URL without verifying whether they are authorized to view that data. This is known as an Insecure Direct Object Reference (IDOR).

Fix Summary

Authorization checks were added to ensure that users can only access their own data.

Security Improvement

This prevents unauthorized users from accessing or modifying other users’ sensitive information.

OWASP Reference

 Broken Access Control

# 2. Cryptographic Failures
Vulnerability Explanation

The original code uses weak hashing algorithms like MD5 and SHA1, which are fast and easily cracked using modern tools.

Fix Summary

Replaced insecure hashing with bcrypt, a slow and secure hashing algorithm that includes salting.

Security Improvement

This makes it significantly harder for attackers to crack passwords, even if hashes are exposed.

OWASP Reference

 Cryptographic Failures

# 3. Injection
Vulnerability Explanation

User input is directly inserted into database queries, allowing attackers to manipulate queries (SQL/NoSQL injection).

Fix Summary

Used parameterized queries and input validation to safely handle user input.

Security Improvement

Prevents attackers from executing arbitrary database commands or accessing unauthorized data.

OWASP Reference

Injection

# 4. Insecure Design
Vulnerability Explanation

The password reset function allows changing a password using only an email address, with no verification step.

Fix Summary

Added a secure token-based password reset process.

Security Improvement

Ensures that only authorized users can reset their passwords.

OWASP Reference

 Insecure Design

# 5. Software and Data Integrity Failures
Vulnerability Explanation

External scripts are loaded without verifying their integrity, which could allow malicious code injection if the source is compromised.

Fix Summary

Implemented Subresource Integrity (SRI) to validate external scripts.

Security Improvement

Ensures that only trusted and untampered scripts are executed.

OWASP Reference

Software and Data Integrity Failures

# 6. Server-Side Request Forgery (SSRF)
Vulnerability Explanation

The application makes requests to URLs provided by users without validation, allowing access to internal systems.

Fix Summary

Restricted requests to trusted domains and validated input URLs.

Security Improvement

Prevents attackers from accessing internal services or sensitive data.

OWASP Reference

Server-Side Request Forgery (SSRF)

# 7. Identification and Authentication Failures
Vulnerability Explanation

Passwords are compared in plaintext, implying they are stored insecurely.

Fix Summary

Implemented secure password hashing and verification using bcrypt.

Security Improvement

Protects user credentials and reduces the risk of account compromise.

OWASP Reference

Identification and Authentication Failures

# Repository Structure

Each vulnerability is organized into its own folder and includes:

Vulnerable code example
Secure (fixed) version of the code
