from retriever import retriever
from validator import validator
from adder import adder

baseURL = "http://127.0.0.1:5000/"
print("n\BLOCKCHAIN'S RELIABILITY TESTS: ")
print("---------------------------------")
adder.test(baseURL)
retriever.test(baseURL)
validator.test(baseURL)