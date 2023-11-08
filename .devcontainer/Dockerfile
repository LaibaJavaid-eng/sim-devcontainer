ARG VARIANT="jammy"
FROM buildpack-deps:${VARIANT}-curl

ARG USERNAME=uazam
ARG USER_UID=1000
ARG USER_GID=$USER_UID

LABEL dev.containers.features="common"

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y sudo \
    && apt-get install -y python3-pip \
    && apt-get install -y openssh-client \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

ENV SHELL /bin/bash


# [Optional] Set the default user. Omit if you want to keep the default as root.
#USER $USERNAME
CMD ["/bin/bash"]

