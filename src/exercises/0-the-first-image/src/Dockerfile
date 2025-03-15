FROM debian:bookworm

RUN apt update
RUN apt install -y cowsay

ENV PATH="$PATH:/usr/games"

ENTRYPOINT ["cowsay", "I hope your day is going well because mine is going"]
CMD ["phenomenal"]
