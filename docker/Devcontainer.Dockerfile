FROM ubuntu:noble

ARG USER_NAME
ARG USER_ID
ARG GROUP_ID

ENV USER_NAME=${USER_NAME:-vscode}

RUN apt -y update
RUN apt -y install \
    sudo ca-certificates curl wget unzip openssh-client lsb-release gnupg git \
    iputils-ping net-tools unzip

# タイムゾーンの設定
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# 環境変数で指定したUID, GID のユーザーを作成
# 既に存在している場合は、ユーザーを削除して作り直す
RUN \
    if getent passwd $USER_ID > /dev/null; then \
        USER_NAME=$(getent passwd $USER_ID | cut -d: -f1); \
        userdel $USER_NAME; \
    fi \
    && if getent group $GROUP_ID > /dev/null; then \
        GROUP_NAME=$(getent group $GROUP_ID | cut -d: -f1); \
        groupdel $GROUP_NAME; \
    fi

RUN groupadd -g $GROUP_ID $USER_NAME
RUN useradd -m -s /bin/bash -u $USER_ID -g $GROUP_ID $USER_NAME
RUN echo "$USER_NAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USER_NAME 

USER $USER_NAME
ENV RYE_HOME /home/${USER_NAME}/.rye
ENV PATH ${RYE_HOME}/shims:${PATH}
ENV LC_ALL C.utf8

# Python の実行環境とライブラリをインストール(Rye を利用)
RUN /bin/bash -o pipefail -c 'curl -sSf https://rye.astral.sh/get -k' | \
    RYE_INSTALL_OPTION="--yes" bash && \
    /home/$USER_NAME/.rye/shims/rye config --set-bool behavior.global-python=true && \
    /home/$USER_NAME/.rye/shims/rye config --set-bool behavior.use-uv=true
RUN /home/$USER_NAME/.rye/shims/rye install flake8
RUN /home/$USER_NAME/.rye/shims/rye install black
RUN echo "export PATH=\$HOME/.rye/shims:\$PATH" >> /home/$USER_NAME/.bashrc
