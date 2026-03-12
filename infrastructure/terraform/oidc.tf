provider "aws" {
  region = "eu-west-1"
}

resource "aws_iam_openid_connect_provider" "github" {
  url = "https://token.actions.githubusercontent.com"

  client_id_list = [
    "sts.amazonaws.com",
  ]

  thumbprint_list = [
    "6938fd4d98bab03faadb97b34396831e3780aea1"
  ]
  
}

resource "aws_iam_role" "github_role" {
  name = "github-actions-gym-tracker"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Federated = aws_iam_openid_connect_provider.github.arn
        }
        Action = "sts:AssumeRoleWithWebIdentity"
        Condition = {
          StringLike = {
            "token.actions.githubusercontent.com:sub" = "repo:AndyMarriottCoder/gym_tracker:*"
          }
        }
      }
    ]
  })
  
}

resource "aws_iam_role_policy_attachment" "test_policy" {
  role       = aws_iam_role.github_role.name
  policy_arn = "arn:aws:iam::aws:policy/ReadOnlyAccess"
}

output "github_role_arn" {
  value = aws_iam_role.github_role.arn
}