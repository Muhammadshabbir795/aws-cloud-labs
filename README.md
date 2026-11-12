# AWS Cloud Labs

Hands-on AWS labs: VPC, EC2, RDS, Lambda, API Gateway, and a CI/CD pipeline.

## CI/CD Lab: GitHub to S3 Deployment Pipeline

### Overview
A static website that deploys to AWS automatically whenever code is pushed to the `main` branch.

### Architecture
GitHub → CodePipeline → S3 Static Website

(Add your draw.io diagram here)

### Tools Used
Git, GitHub, GitHub Actions, AWS CodePipeline, Amazon S3, IAM, CodeConnections

### What I Did
1. Practiced Git: commits, branches, pull requests, merge conflicts, revert, .gitignore
2. Created a GitHub Actions workflow (CI) that checks the project on every push
3. Created an S3 bucket with static website hosting and a public read bucket policy
4. Built a CodePipeline (Source: GitHub, Deploy: S3) connected via GitHub App
5. Pushed a change (v1 to v2) and verified the live website updated

### Screenshots
- Pipeline success
- S3 bucket objects
- Live website v1 and v2
- GitHub Actions green run

### Troubleshooting
| Problem | Cause | Fix |
|---|---|---|
| Website returned 404 (NoSuchKey) | index.html was not in the bucket root | Uploaded the file directly, not inside a folder |
| S3 rejected `cicd-demo/index.html` as index document | Index document cannot contain a slash | Moved index.html to the repo root |
| GitHub Actions CI failed | Workflow still checked the old file path | Updated the path in ci.yml |
| Website still showed v1 after push | Pipeline had not picked up the new commit | Used Release change, then verified the trigger |

### Key Learnings
- CI (GitHub Actions) and CD (CodePipeline) are separate systems
- Folder structure in the repo affects the S3 object path
- Always clean up AWS resources after labs to avoid charges
