title: Git Actions... but wait! RFC4255!
date: 2025-09-07 00:00
status: draft
slug: git-actions-and-rfc4255
lang: en

So we've got [Pelican]({filename}../08/pelican.md) but the fun starts
with deploying it automatically on commit and this is part of what GitHub
Actions is all about. Most of Actions was straight forward and I'll only offer
some details about my setup because if you query your prefered search engine
for "static site deployment with github actions" you'll find plenty to work
with.

GitHub actions is, like, I guess a container that spins up and executes
whatever arbitrary commands from the yaml config file. There's a whole lot
more to it too, but for my purposes it's mostly all about executing commands
as if you were writing a shell script. Upon commit, GitHub spins up a container
and runs the workflows -- your yaml config.

A lot of people use GitHub Pages, and I might explore that in the future, but
for now I have a VPS hosting my site. If I were deploying a website manually I'd
scp the contents to the server, ssh in and move thing to the right place. So...
how do I do this from a container running on GitHub's servers?

First I needed a service account on my VPS. I wanted to limit the user to scp
only but it seems like using scp requires a shell. There's a solution to this,
"scponly", but I've learned the whole thing is deprecated and sftp over ssh is
now preferred since chrooting a user and limiting them to sftp only can be done natively with sshd. Fine, but getting sftp to work with
a one liner in a bash script feels awkward, piping the PUT command into sftp.
Copy everything from the output directory where the site is compiled into the
directory holding my site contents. Since I chrooted the service account to
/var/www/, the relavite path is simply "./vicsimeone/".

    echo "put -r ./output/* ./vicsimeone/" | sftp -i ./id_rsa_webupdate serviceacct@c.w6.io

Ok but to do this with keybased authentication which requires an ssh key? I 
can't just upload a private key to the repository! GitHub repositories has
"secrets" (navigate to your repository > go to *Settings > Security [group]>
Secrets and Variables > Actions* -- and be sure to use "*Repository Secrets*"
not "*Environmental*" which cost me a bit of time). However, you can't pass ssh
a key on the command line, it's got to be a file as far as I know.

Ok, lets encrypt it with AES and we can keep an AES key in GitHub secrets. You
can check my [workflow file](https://github.com/oSquat/vic.sime.one/blob/master/.github/workflows/build-and-deploy.yml)
for the details on loading an environmental variable ($SYMMETRICAL_KEY below)
from GitHub secrets, but the openssl command is shown below, awkward only in
how you provide a decryption key via string on the command line with that
"pass:" prefix.

    # encrypt the private key
    openssl enc -aes-256-cbc -pbkdf2 -in ./id_rsa_webupdate -out ./id_rsa_webupdate.aes

    # decrypt the private key
    openssl enc -d -aes-256-cbc -pbkdf2 -in ./id_rsa_webupdate.aes -out ./id_rsa_webupdate --pass pass:$SYMMETRICAL_KEY

Mission accomplished! No, not yet. Like TLS, ssh not only encrypts your
communication but it also authenticates the server with which you communicate.
If you never connected to the server before (and a freshly created container
would be in this situation) ssh will ask you to verify the public key of the
server by presenting the public key's fingerprint.

To get around this I simply created ~/.ssh and known_hosts with a hardcoded
value but in the process of considering my options I came across RFC4255 
"*Securily Publish SSH Key Fingerprints with DNS*" and I think that may be a
better solution.










