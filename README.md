# gym-tracker


1. Cloned the repo down from GitHub
2. Created the trust between GitHub & AWS via Terraform
  - ISSUE - character in thumbprint wasn't long enough as it was complaining about 40 characters. I added the missing character to overcome the problem. 
3. Ran Terraform init and apply
  - ISSUE - No EC2 IMDS role found. I initially thought it was because I didn't have a token so ran aws login. I had to configure via aws configure and get my access key etc. 
4. Ran Terraform apply and deployed the IAM roles to the account.
  - I wasn't using Root. Logged in with Root to create new role. I was updating old IAM role but this wasn't required. 
5. Configured 