Highcharts.chart('container', {
    chart: {
        type: 'column' // Changed to 'column' for a vertical chart
    },
    title: {
        text: 'Número de donaciones por comuna'
    },
    xAxis: {
        categories: [],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Números',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ' entries'
    },
    series: [{
        name: 'Cantidad',
        data: [] // Replace with actual data if necessary
    }]
});



fetch("http://127.0.0.1:5000/get-grafico-contactos")
  .then((response) => response.json())
  .then((data) => {
    let cantidad = [];
    let comuna = [];
    for (let i = 0; i < data.length; i++) {
      cantidad.push(data[i].cantidad);
      comuna.push(data[i].comuna);
    } 

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container"
    );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: cantidad,
        },
      ],
        xAxis: {
            categories: comuna,
        },
    });
  })
  .catch((error) => console.error("Error:", error));
