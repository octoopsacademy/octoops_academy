# ---------- Stage 1: Build WAR with Maven ----------
FROM maven:3.9.6-eclipse-temurin-17 AS builder

WORKDIR /app

# Copy everything and build
COPY . .
RUN mvn clean package

# ---------- Stage 2: Deploy to Tomcat ----------
FROM tomcat:9.0-jdk17

# Clean default apps (optional)
RUN rm -rf /usr/local/tomcat/webapps/*

# Copy WAR to webapps ROOT
COPY --from=builder /app/target/hello-war.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080

CMD ["catalina.sh", "run"]

