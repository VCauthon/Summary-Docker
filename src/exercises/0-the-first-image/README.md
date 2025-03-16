# Cowsays ....

Generate a docker image using `bookworm` from `debian` as the base image and name your image "cowsay".

The code needed to install the `cowsay` library will be defined on it. The entrypoint will initialize the cowsays program starting with the message "I hope your day is going well because mine is going". And as an argument in the image it will have "phenomenal".

The exercise will be completed if you can initialize the image by displaying the following message:

```bash
 _______________________________________
/ I hope your day is going well because \
\ mine is going phenomenal              /
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Then, without altering the image, you should be able to display the following:

```bash
 _______________________________________
/ I hope your day is going well because \
\ mine is going badly                   /
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

And finally this message:

```bash
 ______________________
< I don't feel very well >
 ------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```


---

## Solution

Using the Dockerfile from [here](./src/Dockerfile) and run the following commands.

- `docker build . -t cowsay`
- `docker run cowsay`
- `docker run badly`
- `docker run --entrypoint /usr/games/cowsay cowsay "I don't feel very well"`

