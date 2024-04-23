# John the Ripper(jtR)

"There are two ways of cracking passwords using John the Ripper. An important aspect of John the Ripper is the wordlist.

Rule-based methods automatically extend the existing wordlist with predefined rules. John the Ripper automatically handles the extension of the existing wordlist.

In script-based methods, we first create a desired sub-wordlist using the existing wordlist and then use John the Ripper."

# Rules

What is a rule?

A rule is a way for John to create variations (rule-based generation of variations) on a wordlist, turning a short wordlist into a much more powerful cracking tool.

List All the Rules: 
```bash
for ruleset in `grep KoreLogicRules ./korelogic-rules-20100801.txt | cut -d: -f 2 | cut -d\] -f 1`; do echo ${ruleset}; done
```

Use specific rule: 
```bash
john --wordlist=rockyou-10.txt --format=wpapsk --rules=KoreLogicRulesPrependYears crackme
```

General command to unhash: 

```bash
john --format=crypt --wordlist=password.lst --rules rules_location grp4_0_hash.txt 
```


Use All the Rules: 

```bash
for ruleset in `grep KoreLogicRules /etc/john/john.conf | cut -d: -f 2 | cut -d\] -f 1`; do john --wordlist=rockyou-10.txt --format=wpapsk --rules=${ruleset} crackme; done
```


A nice subset
```bash
    - grep KoreLogicRules /etc/john/john.conf | cut -d: -f 2 | cut -d\] -f 1 | grep Year | grep -v Special
  
    - for ruleset in `grep KoreLogicRules /etc/john/john.conf | cut -d: -f 2 | cut -d\] -f 1 | grep Year | grep -v Special`; do john --wordlist=rockyou-10.txt --format=wpapsk --rules=${ruleset} crackme; done
```

Unhash password: 

```bash

john --show grp4_0_hash.txt

```

- [Reference](https://charlesreid1.com/wiki/John_the_Ripper/Rules)

## Python script

"In a Python script, we first create the desired sub-wordlist and then apply John the Ripper to the sub-wordlist."
```python

python3 script.py

```