#include <tinyNeoPixel.h>

#define LED_PIN PIN_PC0
#define NUM_LEDS 16
#define TOGGLE_PIN_1 PIN_PA4
#define TOGGLE_PIN_2 PIN_PA5

// Create neopixel object
tinyNeoPixel pixels = tinyNeoPixel(NUM_LEDS, LED_PIN, NEO_GRB);

// Array to map physical LED positions to logical positions due to serpentine wiring
const uint8_t ledMap[NUM_LEDS] = {
  0,  1,  2,  3,      // First row ->
  7,  6,  5,  4,      // Second row <-
  8,  9,  10, 11,     // Third row ->
  15, 14, 13, 12      // Fourth row <-
};

void setup() {
  // Initialize neopixel library
  pixels.begin();

  // Clear all pixels
  pixels.clear();
  pixels.show();

  tinypixel();

  // Configure toggle pins as outputs
  pinMode(TOGGLE_PIN_1, OUTPUT);
  pinMode(TOGGLE_PIN_2, OUTPUT);
}

void loop() {
  // Toggle PA4
  analogWrite(TOGGLE_PIN_1, 10);
  delay(500);
  analogWrite(TOGGLE_PIN_1, 0);
  delay(500);

  // Toggle PA5
  analogWrite(TOGGLE_PIN_2, 5);
  delay(500);
  analogWrite(TOGGLE_PIN_2, 0);
  delay(500);

  tinypixel();
}

void tinypixel() {
  // Light up LEDs one by one with a blue color
  pixels.clear();
  for (int i = 0; i < NUM_LEDS; i++) {
    pixels.setPixelColor(ledMap[i], pixels.Color(0, 0, 5)); // Blue color at medium brightness
    pixels.show();
    delay(50); // Wait 100ms between each LED
  }
}
