FROM docker.elastic.co/logstash/logstash:8.7.1

# 플러그인 설치
RUN /usr/share/logstash/bin/logstash-plugin install logstash-output-mongodb

# 설정 파일 복사
COPY logstash.conf /usr/share/logstash/pipeline/logstash.conf
COPY logstash.yml /usr/share/logstash/config/logstash.yml