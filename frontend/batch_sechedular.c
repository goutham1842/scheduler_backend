//CH.SC.U4CSE24064
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int id;
    int compute;
    int deadline;
    float priority;
} Job;

int today = 1;

/* Function to calculate priority */
float calculatePriority(int compute, int deadline)
{
    int urgency = deadline - today;
    if (urgency < 0)
        urgency = 0;

    float p = (1.0 / (urgency + 1)) + (1.0 / compute);
    return p;
}

/* Comparison function for sorting (descending priority) */
int compare(const void *a, const void *b)
{
    Job *j1 = (Job *)a;
    Job *j2 = (Job *)b;

    if (j1->priority < j2->priority)
        return 1;
    else if (j1->priority > j2->priority)
        return -1;
    else
        return 0;
}

int main()
{
    int k, N,i;

    printf("Enter number of jobs: ");
    scanf("%d", &k);

    Job jobs[k];

    printf("\nEnter compute units and deadlines\n");

    for ( i = 0; i < k; i++)
    {
        jobs[i].id = i + 1;

        printf("\nJob J%d\n", i + 1);
        printf("Compute Units: ");
        scanf("%d", &jobs[i].compute);

        printf("Deadline (day): ");
        scanf("%d", &jobs[i].deadline);

        jobs[i].priority = calculatePriority(jobs[i].compute, jobs[i].deadline);
    }

    printf("\nEnter number of jobs to schedule today (N): ");
    scanf("%d", &N);

    /* Sort jobs based on priority */
    qsort(jobs, k, sizeof(Job), compare);

    printf("\n---- Job Priorities ----\n");

    for (i = 0; i < k; i++)
    {
        printf("Job J%d | Compute: %d | Deadline: %d | Priority: %.2f\n",
               jobs[i].id,
               jobs[i].compute,
               jobs[i].deadline,
               jobs[i].priority);
    }

    printf("\n---- Selected Jobs For Today ----\n");

    for (i = 0; i < N && i < k; i++)
    {
        printf("Execute Job J%d (Compute=%d, Deadline=%d)\n",
               jobs[i].id,
               jobs[i].compute,
               jobs[i].deadline);
    }

    return 0;
}
