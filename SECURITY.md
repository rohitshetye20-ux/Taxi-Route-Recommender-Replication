# Security Policy

## Supported Versions

The following versions of the project currently receive security updates.

| Version | Supported |
|---------|:---------:|
| 1.0.x | ✅ Yes |
| < 1.0 | ❌ No |

Only the latest stable release is actively maintained for security-related issues.

---

# Reporting a Security Vulnerability

If you discover a potential security vulnerability in this repository, please **do not disclose it publicly before it has been reviewed**.

Instead, please report it responsibly by contacting the project maintainer through GitHub.

You can:

- Open a private security advisory (if GitHub Security Advisories are enabled).
- Contact the maintainer through GitHub.
- If private reporting is unavailable, open a GitHub Issue **without disclosing sensitive exploit details**, and the maintainer will provide further instructions.

Please include:

- A clear description of the issue.
- Steps to reproduce the vulnerability.
- The affected files or components.
- The potential impact.
- Any suggested mitigation (if known).

Providing sufficient detail helps us investigate and resolve issues more efficiently.

---

# Response Process

When a valid security report is received, the following process will be followed:

1. Acknowledge receipt of the report.
2. Investigate and reproduce the issue.
3. Assess the severity and impact.
4. Develop and test a fix, if required.
5. Release an update when appropriate.
6. Publicly document the fix in the project changelog after the issue has been addressed.

The goal is to respond promptly while protecting users from unnecessary exposure.

---

# Scope

This policy applies to:

- Python source code
- Report Builder framework
- Presentation Builder framework
- Documentation generation scripts
- Repository automation utilities
- Configuration files

It does **not** apply to:

- The original research paper.
- Third-party datasets.
- External libraries or frameworks (such as TensorFlow, NumPy, or python-docx).
- GitHub platform services.

Security issues affecting third-party software should be reported directly to the maintainers of those respective projects.

---

# What Should Be Reported

Examples of security issues include:

- Accidental exposure of credentials or API keys.
- Vulnerabilities that could allow arbitrary code execution.
- Unsafe handling of untrusted input.
- Dependency vulnerabilities affecting this project.
- Malicious code introduced through contributions.
- Sensitive information committed to the repository.

---

# What Should Not Be Reported

The following should be reported through normal GitHub Issues instead:

- Installation problems.
- Documentation errors.
- Feature requests.
- Performance improvements.
- Machine learning model accuracy.
- Reproducibility questions.
- Dataset-related issues.
- General coding bugs that do not create a security risk.

---

# Dependency Security

This project relies on several open-source Python libraries.

Contributors are encouraged to:

- Keep dependencies up to date.
- Monitor dependency advisories.
- Review changes before upgrading major versions.
- Avoid introducing unnecessary dependencies.

Security-related dependency updates should include testing to ensure they do not affect reproducibility.

---

# Responsible Disclosure

Please allow reasonable time for investigation and remediation before publicly disclosing a confirmed vulnerability.

Responsible disclosure helps protect users while allowing maintainers to prepare and verify an appropriate fix.

---

# Security Best Practices for Contributors

When contributing to this repository:

- Never commit passwords, tokens, API keys, or secrets.
- Do not include personal credentials in notebooks or scripts.
- Review code before submitting Pull Requests.
- Keep local development environments updated.
- Use virtual environments for dependency isolation.
- Verify external resources before incorporating them into the project.

---

# Contact

For security-related concerns, please use GitHub to contact the project maintainer.

Repository:

https://github.com/rohitshetye20-ux/Taxi-Route-Recommender

---

# Acknowledgement

We appreciate the efforts of security researchers, contributors, and community members who responsibly report potential vulnerabilities and help improve the security of this project.

Thank you for helping keep this repository safe for everyone.