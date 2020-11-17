#!/usr/bin/env bash

shuffled_features="$(shuf -e story01_categorize_tasks_priority.feature story02_add_task_course.feature story03_mark_task_done.feature story04_remove_task_course.feature story05_create_todo_list.feature story06_remove_todo_list.feature story10_change_task_description.feature)"

# convert '\n' delimited string to array
readarray -t FEATURES <<<"$shuffled_features"

# remove previous log file if exists
rm -f logs_random_order.txt

# test features in random order
for FEATURE in "${FEATURES[@]}"; do
    # log section
    echo  $'\n--------'$FEATURE$'--------'>> logs_random_order.txt

    # run random feature and log summary only
    behave "features/$FEATURE" -f null | tee -a logs_random_order.txt
done
