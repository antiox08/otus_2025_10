FROM python:3.12

WORKDIR /app

# # Установим зависимости для браузеров
# RUN apt-get update && apt-get install -y \
#     wget unzip curl gnupg2 \
#     libnss3 libfontconfig1 libxss1 libappindicator3-1 libasound2 \
#     firefox-esr \
#     && rm -rf /var/lib/apt/lists/*

# # Установка Google Chrome
# RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
#     && dpkg -i google-chrome-stable_current_amd64.deb || apt-get -fy install \
#     && rm google-chrome-stable_current_amd64.deb
#
# # Установка Chromedriver
# RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+') \
#     && wget -q "https://chromedriver.storage.googleapis.com/${CHROME_VERSION}/chromedriver_linux64.zip" \
#     && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
#     && rm chromedriver_linux64.zip \
#     && chmod +x /usr/local/bin/chromedriver
#
# # Установка geckodriver для Firefox
# RUN wget -q https://github.com/mozilla/geckodriver/releases/latest/download/geckodriver-v0.34.0-linux64.tar.gz \
#     && tar -xzf geckodriver-v0.34.0-linux64.tar.gz -C /usr/local/bin/ \
#     && rm geckodriver-v0.34.0-linux64.tar.gz \
#     && chmod +x /usr/local/bin/geckodriver

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["pytest"]
