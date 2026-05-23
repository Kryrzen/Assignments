# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: VinoshanModPackage
# Description: A package for converting temperature and distance units.

def fahrenheit_to_celsius(fahrenheit):
    # Converts to Celsius
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    # COnverts to Fahrenheit
    return (celsius * 9 / 5) + 32