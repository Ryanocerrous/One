# One

1. This is my first Repo and its not working

2. Starting to figure out the basics

3. Im updating and pushing this file. 

4. Success! I'll try once more... 

5. Final test to show I know clone/commit/add/push.

6. Completed test.


How I completed the push of this file:

ryan@Ryans-M1 code % cd
ryan@Ryans-M1 ~ % git clone https://github.com/Ryanocerrous/One.git
Cloning into 'One'...
remote: Enumerating objects: 42, done.
remote: Counting objects: 100% (42/42), done.
remote: Compressing objects: 100% (34/34), done.
remote: Total 42 (delta 9), reused 9 (delta 2), pack-reused 0
Receiving objects: 100% (42/42), 10.06 KiB | 343.00 KiB/s, done.
Resolving deltas: 100% (9/9), done.
ryan@Ryans-M1 ~ % cd
ryan@Ryans-M1 ~ % cd desktop
ryan@Ryans-M1 desktop % git clone https://github.com/Ryanocerrous/One.git
Cloning into 'One'...
remote: Enumerating objects: 42, done.
remote: Counting objects: 100% (42/42), done.
remote: Compressing objects: 100% (34/34), done.
remote: Total 42 (delta 9), reused 9 (delta 2), pack-reused 0
Receiving objects: 100% (42/42), 10.06 KiB | 312.00 KiB/s, done.
Resolving deltas: 100% (9/9), done.
ryan@Ryans-M1 desktop % cd one
ryan@Ryans-M1 one % git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
ryan@Ryans-M1 one % git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Turn this message off by running
hint: "git config advice.addEmptyPathspec false"
ryan@Ryans-M1 one % git commit -a -m "Completed test"
[main 2d773b5] Completed test
 1 file changed, 2 insertions(+)
ryan@Ryans-M1 one % git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Ryanocerrous/One.git
   dcbfc40..2d773b5  main -> main
ryan@Ryans-M1 one % git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
ryan@Ryans-M1 one % 
