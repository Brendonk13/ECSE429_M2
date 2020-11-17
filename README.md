# BDD test suite for todo manager API

Group: AutoProj 25

## Setup
> pip install behave

## Ensure 'todo manager API' is running on localhost:4567
> java -jar runTodoManagerRestAPI-1.5.5.jar

## Option 1) Run all tests (all features/ user stories)
> behave -v

Get summary log using:
> behave -f null | tee logs_normal_order.txt

## Option 2) Run all tests in random order
> From root directory containing README.md: bash random_order_behave.sh

Summary log recorded in logs_random_order.txt

## Option 3) Run a single feature file manually
> behave -i <story_feature_filename>.feature
