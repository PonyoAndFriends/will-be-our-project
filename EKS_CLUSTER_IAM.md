- EKS 클러스터 삭제, EKS 클러스터 생성을 깃헙 액션에서 가능하도록 IaC를 구성했습니다.

- 아래를 참고하셔서 IAM 유저를 생성하고 권한을 부여합니다.

- 해당 유저의 액세스 키와 시크릿 키를 깃허브 시크릿으로 관리하고, 코드로 EKS를 띄우고 내립니다.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "eks:DescribeCluster",
        "eks:DeleteCluster"
      ],
      "Resource": "*"
    }
  ]
}
```