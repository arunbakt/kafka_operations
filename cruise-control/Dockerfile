FROM eclipse-temurin:17.0.7_7-jdk as cruisecontrol
# Install necessary tools
RUN apt-get update && apt-get install -y git maven

# Set working directory
WORKDIR /usr/src/cruise-control

# Clone the Cruise Control repository
RUN git clone https://github.com/linkedin/cruise-control.git .

# Build the Cruise Control project
RUN ./gradlew jar copyDependantLibs

# Expose the default Cruise Control port
EXPOSE 9091
EXPOSE 5005

# Set configuration file locations
ENV CRUISE_CONTROL_HOME=/usr/src/cruise-control
ENV CRUISE_CONTROL_CONFIG_PATH=$CRUISE_CONTROL_HOME/config/cruisecontrol.properties
ENV CRUISE_CONTROL_LOG4J_PATH=$CRUISE_CONTROL_HOME/config/log4j2.xml
ENV JAVA_TOOL_OPTIONS "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005"

# Copy default configuration files
COPY config/cruisecontrol.properties $CRUISE_CONTROL_CONFIG_PATH
COPY config/log4j2.xml $CRUISE_CONTROL_LOG4J_PATH
COPY config/capacity.json $CRUISE_CONTROL_HOME/config/capacity.json
# Start Cruise Control
ENTRYPOINT ["./kafka-cruise-control-start.sh", "config/cruisecontrol.properties"]
