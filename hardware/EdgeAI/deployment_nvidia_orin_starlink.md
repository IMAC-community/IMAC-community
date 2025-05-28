# Edge AI Deployment: NVIDIA Jetson Orin Nano with Starlink

## System Overview

**Deployment Name:** IMAC-ORIN-STARLINK-001  
**Version:** 1.0  
**Last Updated:** 2024-01-15  
**Maintainer:** IMAC Hardware Pod Team (hardware@imac-consortium.org)  
**Status:** Production

### Purpose & Objectives
This deployment creates a remote marine monitoring station capable of real-time AI inference with satellite connectivity. The system is designed for deployment in remote ocean locations where traditional connectivity is unavailable, enabling continuous monitoring of marine life, water quality, and environmental conditions.

### Key Capabilities
- [x] Real-time species identification from underwater cameras
- [x] Edge-based anomaly detection for environmental monitoring
- [x] Satellite data transmission via Starlink
- [x] 24/7 autonomous operation with solar power
- [x] Remote management and model updates

---

## Hardware Specifications

### Compute Module
**Model:** NVIDIA Jetson Orin Nano 8GB  
**CPU:** 6-core Arm Cortex-A78AE v8.2 64-bit CPU  
**GPU:** 1024-core NVIDIA Ampere architecture GPU with 32 Tensor Cores  
**Memory:** 8GB 128-bit LPDDR5 (68 GB/s)  
**Storage:** 512GB NVMe SSD (Samsung 980)  
**AI Performance:** Up to 40 TOPS

### Power System
**Power Requirements:** 7W-15W (configurable power modes)  
**Power Source:** 
- Primary: 100W Solar Panel with MPPT Controller
- Battery: 12V 100Ah LiFePO4 Battery
- Backup: 12V DC input from vessel power
**Runtime:** 72 hours on battery (low power mode)  
**Power Management:** 
- Dynamic power scaling based on workload
- Sleep mode during low activity periods
- Wake-on-motion from camera feed

### Connectivity
**Primary Network:** Starlink Maritime  
**Backup Network:** Iridium satellite modem  
**Data Rates:** 
- Starlink: 50-200 Mbps (typical)
- Iridium: 2.4 kbps (emergency backup)
**Protocols:** MQTT over TLS for telemetry, HTTPS for data upload

### Environmental Protection
**Enclosure:** Nanuk 905 Waterproof Case  
**IP Rating:** IP67  
**Operating Temperature:** -25°C to 50°C  
**Humidity Tolerance:** 10% to 90% (non-condensing)  
**Additional Protection:** 
- Desiccant packs for humidity control
- Thermal management with passive heatsinks
- Shock-absorbing mounting

### Sensors & Peripherals
| Device | Model | Interface | Purpose |
|--------|-------|-----------|---------|
| Underwater Camera | Blue Robotics Low-Light HD | USB 3.0 | Species monitoring |
| Environmental Sensor | Atlas Scientific EZO | I2C | pH, temp, dissolved O2 |
| GPS Module | SparkFun ZOE-M8Q | UART | Location tracking |
| IMU | Bosch BNO055 | I2C | Motion detection |
| Hydrophone | Aquarian H2a | USB Audio | Marine mammal detection |

---

## Software Stack

### Operating System
**OS:** NVIDIA JetPack 5.1.2 (Ubuntu 20.04-based)  
**Kernel:** Linux 5.10.104-tegra  
**Real-time Support:** Yes (PREEMPT_RT patches applied)

### AI Framework
**Primary Framework:** ONNX Runtime with TensorRT backend  
**Version:** ONNX Runtime 1.16.0, TensorRT 8.5.2  
**Optimization:** 
- INT8 quantization for supported models
- Multi-stream inference for parallel processing
- Dynamic batching for efficiency

### Runtime Dependencies
```
# Core AI/ML
onnxruntime-gpu==1.16.0
tensorrt==8.5.2
opencv-python==4.8.0.74
numpy==1.24.3
pillow==10.0.0

# Communication
paho-mqtt==1.6.1
requests==2.31.0
protobuf==4.23.4

# Sensor Integration
pyserial==3.5
smbus2==0.4.2
adafruit-circuitpython-bno055==5.4.0

# System Monitoring
psutil==5.9.5
nvidia-ml-py==12.535.77
```

### Container Configuration
**Container Platform:** Docker 24.0.5  
**Base Image:** nvcr.io/nvidia/l4t-ml:r35.3.1-py3  
**Registry:** ghcr.io/imac-consortium/edge-ai

---

## AI Models

### Model Details
| Model Name | Version | Purpose | Input | Output | Size |
|------------|---------|---------|-------|--------|------|
| marine_species_yolov8 | v2.3 | Fish species detection | 640x480 RGB | Bounding boxes + species | 45MB |
| anomaly_detector | v1.2 | Environmental anomalies | Sensor array | Anomaly score | 12MB |
| whale_classifier | v3.1 | Whale sound classification | Audio spectrogram | Species + confidence | 28MB |
| coral_health | v1.5 | Coral bleaching detection | 1024x768 RGB | Health score map | 67MB |

### Performance Metrics
**Inference Time:** 
- Species detection: 25ms @ 640x480
- Anomaly detection: 5ms per reading
- Whale classification: 100ms per 10s clip
**Throughput:** 40 FPS for video analysis  
**Accuracy:** 
- Species detection: 94.2% mAP
- Anomaly detection: 98.5% F1 score
- Whale classification: 91.7% accuracy
**Resource Usage:** 
- GPU: 75% average utilization
- CPU: 45% average (2 cores)
- Memory: 4.2GB average

---

## Deployment Configuration

### Installation Steps
1. **Base System Setup**
   ```bash
   # Flash JetPack 5.1.2 to Orin Nano
   sudo apt update && sudo apt upgrade -y
   # Install Docker and prerequisites
   ```

2. **Hardware Integration**
   ```bash
   # Configure I2C for sensors
   sudo i2cdetect -y -r 1
   # Set up camera permissions
   sudo usermod -a -G video $USER
   ```

3. **Starlink Configuration**
   - Connect Ethernet from Starlink router to Jetson
   - Configure static IP: 192.168.1.100
   - Set up port forwarding for remote access

4. **Deploy Edge AI Stack**
   ```bash
   docker compose -f edge-ai-compose.yml up -d
   ```

5. **Validation Tests**
   ```bash
   python3 /opt/imac/tests/system_check.py
   ```

### Configuration Files
**System Config:** `/opt/imac/config/system.yaml`  
**Model Config:** `/opt/imac/config/models.json`  
**Service Config:** `/etc/systemd/system/imac-edge.service`

### Data Management
**Input Sources:** 
- Continuous video stream from underwater camera
- Sensor readings every 30 seconds
- Audio clips triggered by amplitude threshold
**Storage Strategy:** 
- Local: 7 days rolling buffer (100GB)
- Cloud: Processed results and alerts only
- Archive: Raw data on detection events
**Preprocessing:** 
- Video: Resize, normalize, format conversion
- Sensors: Calibration correction, outlier filtering
- Audio: FFT, mel-spectrogram generation

### Communication Setup
**Upstream Endpoint:** https://api.imac-consortium.org/v1/edge  
**Message Format:** Protocol Buffers with gzip compression  
**Queue Management:** 
- Local queue: 10,000 messages
- Priority levels for alerts vs routine data
**Telemetry Frequency:** 
- System health: Every 5 minutes
- Sensor data: Every 30 seconds
- Detections: Real-time with 1s debounce

---

## Operational Procedures

### Startup Sequence
1. Power on → Boot loader (15s)
2. Linux kernel boot → SystemD init (45s)
3. Docker containers start (30s)
4. Starlink connection established (2-3 min)
5. AI models loaded to GPU (20s)
6. Begin data collection and inference

### Monitoring & Diagnostics
**Health Metrics:** 
- CPU temp: Warning >70°C, Critical >85°C
- GPU temp: Warning >75°C, Critical >87°C
- Memory usage: Warning >85%, Critical >95%
- Storage: Warning <10GB free, Critical <1GB
**Performance Metrics:** 
- Inference latency P95 < 50ms
- Data backlog < 1000 messages
- Starlink signal quality > -80 dBm
**Log Location:** `/var/log/imac/`  
**Alert Thresholds:** Configured in Prometheus rules

### Maintenance Schedule
| Task | Frequency | Procedure |
|------|-----------|-----------|
| System updates | Monthly | Ansible playbook via satellite |
| Model updates | Bi-weekly | Docker image pull during low usage |
| Camera cleaning | Monthly | Manual cleaning during site visit |
| Battery check | Quarterly | Voltage and capacity test |
| Full backup | Weekly | Automated to cloud storage |

### Troubleshooting Guide
| Issue | Symptoms | Solution |
|-------|----------|----------|
| No Starlink connection | No internet, status LED red | 1. Check cable connections<br>2. Power cycle Starlink<br>3. Check obstruction map |
| High inference latency | >100ms processing time | 1. Check GPU temperature<br>2. Reduce power mode<br>3. Restart AI service |
| Sensor read failures | Missing data, I2C errors | 1. Check I2C connections<br>2. Run sensor diagnostic<br>3. Replace faulty sensor |
| Storage full | System sluggish, write errors | 1. Check log rotation<br>2. Clear old video cache<br>3. Increase cloud upload |

---

## Security Considerations

### Access Control
**Authentication:** SSH key-based + 2FA for remote access  
**Authorization:** Role-based access control (RBAC)  
**Encryption:** 
- Storage: LUKS full-disk encryption
- Network: TLS 1.3 for all communications
- Models: Encrypted model files

### Update Management
**Update Method:** Automated OTA via Starlink during maintenance window  
**Rollback Strategy:** A/B partition scheme with automatic rollback on failure  
**Signing:** All updates signed with IMAC consortium key

---

## Cost Analysis

### Hardware Costs
| Component | Unit Cost | Quantity | Total |
|-----------|-----------|----------|-------|
| Jetson Orin Nano Dev Kit | $499 | 1 | $499 |
| Starlink Maritime Kit | $2,500 | 1 | $2,500 |
| Nanuk 905 Case | $149 | 1 | $149 |
| Solar Panel (100W) | $120 | 1 | $120 |
| LiFePO4 Battery (100Ah) | $380 | 1 | $380 |
| Sensors & Cameras | $850 | 1 | $850 |
| Mounting & Cables | $200 | 1 | $200 |
| **Total Hardware** | | | **$4,698** |

### Operational Costs
**Power:** $0 (solar powered)  
**Connectivity:** $250/month (Starlink Maritime)  
**Maintenance:** $500/year (estimated)  
**Total TCO:** $3,500/year

---

## Performance Benchmarks

### Test Conditions
**Dataset:** IMAC Marine Test Set v2.0 (10,000 images, 100 hours audio)  
**Duration:** 30-day continuous operation  
**Environment:** Deployed at Hawaiian reef monitoring station

### Results
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Species Detection Accuracy | 90% | 94.2% | ✅ |
| Inference Latency (P95) | <50ms | 42ms | ✅ |
| System Uptime | 99% | 99.7% | ✅ |
| Data Transmission Success | 95% | 98.3% | ✅ |
| Power Efficiency | <15W avg | 11.2W | ✅ |
| False Positive Rate | <5% | 3.1% | ✅ |

---

## Deployment History

| Date | Version | Changes | Deployed By |
|------|---------|---------|-------------|
| 2023-10-15 | v0.1 | Initial prototype testing | J. Smith |
| 2023-11-20 | v0.5 | Added Starlink integration | M. Chen |
| 2023-12-10 | v0.8 | Multi-model support | K. Patel |
| 2024-01-15 | v1.0 | Production deployment | Hardware Team |

---

## References & Resources

### Documentation
- [NVIDIA Jetson Orin Nano Developer Guide](https://developer.nvidia.com/embedded/jetson-orin-nano-developer-kit)
- [Starlink Maritime Setup Guide](https://www.starlink.com/maritime)
- [IMAC Edge AI Deployment Manual](https://docs.imac-consortium.org/edge-ai)

### Support Contacts
- **Technical Support:** edge-support@imac-consortium.org
- **Community Forum:** https://forum.imac-consortium.org/edge-ai
- **Issue Tracker:** https://github.com/imac-consortium/edge-deployments/issues

### Related Deployments
- [Coral Reef Monitor (Raspberry Pi Version)](./deployment_rpi_coral_reef.md)
- [Acoustic Array (Jetson Xavier NX)](./deployment_xavier_acoustic.md)
- [Drone-based Survey System](./deployment_orin_drone.md)
