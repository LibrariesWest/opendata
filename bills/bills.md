Bills
=====

#### Summary file

The summary gives basic data about the number of bills generated in the Library Management System, separated by bill reason and library authority.

- [Download bills summary data](https://github.com/LibrariesWest/opendata/blob/master/bills/bills_summary.csv)

| Field | Description | Example |
| ----- | ----------- | ------- |
| Financial year billed | The financial year the bill record was created | 2017/2018 |
| Bill authority | The authority the bill record was created for | Somerset |
| Bill reason | The reason for the bill | HOLD |
| Number of bills | The number of bills included in this grouping | 5 |
| Total billed | The total amount billed in pounds | 5 |

{% chartjs %}
{
    type: 'bar',
    data: {
        labels: ["Testing"],
        datasets: [{
            label: 'Bills',
            data: [18, 25, 20, 23, 17, 13, 18],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255,99,132,1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
}
{% endchartjs %}


#### Detail file

For more detail use this download, the columns included are described below.

- Coming soon

| Field | Description | Example |
| ----- | ----------- | ------- |
| Month billed | The month the bill record was created | 2017-11 |
| Bill authority | The authority the bill record was created for | Somerset |
| Bill library | The library the bill was created for | Taunton |
| Item type | The type of item that the bill record is for | ADU_FIC |
| Bill reason | The reason for the bill | HOLD |
| Number of bills | The number of bills included in this grouping | 5 |
| Total billed | The total amount billed in pounds | 5 |
