## Database security

![Who needs access and why?](./img/robber.jpg)

You'll want to [limit risk as much as possible](https://www.ibm.com/developerworks/opensource/library/os-postgresecurity/), so database security is a **must**!

1. Stop hackers
2. Limit access
3. Avoid data problems

First things first: **never use root**! The default user (root) has unlimited access to your database — imagine if the guy above had access to that?

1. Set a strong password for _root_
    + On `local` and `live`
2. Never [commit your password to a repo](https://stackoverflow.com/q/2820831)
3. Keep it [secret](https://bit.ly/2By51sf), keep it [safe](https://stackoverflow.com/q/9832648)


**Ask someone who knows what they're doing** if setting a password on `root` is required in Postgres (it's a bit different and [you can use `psql`](https://stackoverflow.com/q/9832648))
