function DHT11 () {
    NPNLCD.clear()
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P0,
    true,
    false,
    true
    )
    humid_var = dht11_dht22.readData(dataType.humidity)
    temp_var = dht11_dht22.readData(dataType.temperature)
    NPNLCD.ShowString("Temp: " + ("" + temp_var), 0, 0)
    // NPNLCD.ShowString("Humid: " + ("" + humid_var), 0, 1)
    serial.writeString("!TEMP:" + ("" + temp_var) + "#")
    // NPNLCD.ShowString("Humid: " + ("" + humid_var), 0, 1)
    serial.writeString("!HUMID:" + ("" + humid_var) + "#")
}
function LED_control () {
    if (mode == 0) {
        if (LED_manual == 1) {
            pins.digitalWritePin(DigitalPin.P4, 1)
            NPNLCD.ShowString("Turn on LED", 0, 1)
            serial.writeString("!LED:" + "1" + "#")
        } else {
            pins.digitalWritePin(DigitalPin.P4, 0)
            NPNLCD.ShowString("Turn off LED", 0, 1)
            serial.writeString("!LED:" + "0" + "#")
        }
    } else {
        if (light_var > 300) {
            pins.digitalWritePin(DigitalPin.P4, 0)
            NPNLCD.ShowString("Turn off LED", 0, 1)
            serial.writeString("!LED:" + "0" + "#")
        } else {
            pins.digitalWritePin(DigitalPin.P4, 1)
            NPNLCD.ShowString("Turn on LED", 0, 1)
            serial.writeString("!LED:" + "1" + "#")
        }
    }
}
serial.onDataReceived(serial.delimiters(Delimiters.Hash), function () {
    receivedMsg = serial.readUntil(serial.delimiters(Delimiters.Hash))
    receivedMsg = "" + receivedMsg.slice(1)
    splitData = receivedMsg.split(":")
    if (splitData[0] == "bbc-mode") {
        if (splitData[1] == "1") {
            mode = 1
        } else {
            mode = 0
        }
    } else if (splitData[0] == "bbc-led") {
        if (splitData[1] == "1") {
            LED_manual = 1
        } else {
            LED_manual = 0
        }
        LED_control()
    } else if (splitData[0] == "bbc-pump") {
        if (splitData[1] == "1") {
            pump_manual = 1
        } else {
            pump_manual = 0
        }
        Pump_control()
    } else if (splitData[0] == "bbc-fan") {
        if (splitData[1] == "2") {
            fan_manual = 2
        } else if (splitData[1] == "1") {
            fan_manual = 1
        } else {
            fan_manual = 0
        }
        Fan_control()
    } else {
    	
    }
})
function Pump_control () {
    if (mode == 0) {
        if (pump_manual == 1) {
            NPNBitKit.Relay(DigitalPin.P2, true)
            NPNLCD.ShowString("Turn on pump", 0, 1)
            serial.writeString("!PUMP:" + "1" + "#")
        } else {
            NPNBitKit.Relay(DigitalPin.P2, false)
            NPNLCD.ShowString("Turn off pump", 0, 1)
            serial.writeString("!PUMP:" + "0" + "#")
        }
    } else {
        if (NPNBitKit.AnalogSoilMosture(AnalogPin.P3) < 30) {
            NPNBitKit.Relay(DigitalPin.P2, true)
            NPNLCD.ShowString("Turn on pump", 0, 1)
            serial.writeString("!PUMP:" + "1" + "#")
        } else {
            NPNBitKit.Relay(DigitalPin.P2, false)
            NPNLCD.ShowString("Turn off pump", 0, 1)
            serial.writeString("!PUMP:" + "0" + "#")
        }
    }
}
function Fan_control () {
    if (mode == 0) {
        if (fan_manual == 2) {
            pins.digitalWritePin(DigitalPin.P8, 0)
            pins.analogWritePin(AnalogPin.P9, 500)
            NPNLCD.ShowString("Fan: ON lv 2", 0, 1)
            serial.writeString("!FAN:" + "2" + "#")
        } else if (fan_manual == 1) {
            pins.digitalWritePin(DigitalPin.P8, 0)
            pins.analogWritePin(AnalogPin.P9, 300)
            NPNLCD.ShowString("Fan: ON lv 1", 0, 1)
            serial.writeString("!FAN:" + "1" + "#")
        } else {
            pins.analogWritePin(AnalogPin.P9, 0)
            NPNLCD.ShowString("Fan: OFF", 0, 1)
            serial.writeString("!FAN:" + "0" + "#")
        }
    } else {
        if (temp_var > 35) {
            pins.digitalWritePin(DigitalPin.P8, 1)
            pins.analogWritePin(AnalogPin.P9, 500)
            NPNLCD.ShowString("Fan: ON lv 2", 0, 1)
            serial.writeString("!FAN:" + "2" + "#")
        } else if (temp_var > 20) {
            pins.digitalWritePin(DigitalPin.P8, 1)
            pins.analogWritePin(AnalogPin.P9, 300)
            NPNLCD.ShowString("Fan: ON lv 1", 0, 1)
            serial.writeString("!FAN:" + "1" + "#")
        } else {
            pins.analogWritePin(AnalogPin.P9, 1)
            NPNLCD.ShowString("Fan: OFF", 0, 1)
            serial.writeString("!FAN:" + "0" + "#")
        }
    }
}
function Auto_light () {
    NPNLCD.clear()
    light_var = pins.analogReadPin(AnalogPin.P1)
    NPNLCD.ShowString("Light: " + ("" + light_var), 0, 0)
    serial.writeString("!LIGHT:" + ("" + light_var) + "#")
}
function Moisture_sensor () {
    NPNLCD.clear()
    soil_var = NPNBitKit.AnalogSoilMosture(AnalogPin.P3)
    NPNLCD.ShowString("Soil: " + ("" + soil_var), 0, 0)
    serial.writeString("!SOIL:" + ("" + soil_var) + "#")
}
let clk_count = 0
let soil_var = 0
let fan_manual = 0
let pump_manual = 0
let splitData: string[] = []
let light_var = 0
let LED_manual = 0
let temp_var = 0
let humid_var = 0
let mode = 0
let receivedMsg = ""
NPNLCD.LcdInit()
led.enable(false)
mode = 1
basic.forever(function () {
    clk_count = (clk_count + 1) % 3
    if (clk_count == 0) {
        DHT11()
        Fan_control()
    }
    if (clk_count == 1) {
        Auto_light()
        LED_control()
    }
    if (clk_count == 2) {
        Moisture_sensor()
        Pump_control()
    }
    basic.pause(7000)
})
