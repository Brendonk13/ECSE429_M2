#!/usr/bin/env bash

shuffled_features="$(shuf -e story01_categorize_tasks_priority.feature story05_create_todo_list.feature story06_remove_todo_list.feature story10_change_task_description.feature)"

# convert '\n' delimited string to array
readarray -t FEATURES <<<"$shuffled_features"

for FEATURE in "${FEATURES[@]}"; do
    # echo -e "feature: $FEATURE\n\n"
    behave "features/$FEATURE"
done
