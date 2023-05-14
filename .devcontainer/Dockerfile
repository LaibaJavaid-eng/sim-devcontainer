ARG VARIANT="jammy"
FROM buildpack-deps:${VARIANT}-curl

LABEL dev.containers.features="common"

# [Optional] Uncomment this section to install additional OS packages.
#RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#    && apt-get -y install --no-install-recommends \
#        build-essential

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_$(dpkg --print-architecture).deb -o /tmp/chrome.deb \
    && apt-get -y install /tmp/chrome.deb \
    && apt-get -y install --no-install-recommends \
        build-essential