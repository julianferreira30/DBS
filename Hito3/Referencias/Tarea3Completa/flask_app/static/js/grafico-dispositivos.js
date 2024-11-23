Highcharts.chart('container', {
    chart: {
        type: 'pie', // Set to 'pie' for a pie chart
    },
    title: {
        text: 'Cantidad de dispositivos por tipo'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.y}</b> entries'
    },
    series: [{
        name: 'Entries',
        colorByPoint: true,
        data: []
    }]
});

fetch("http://127.0.0.1:5000/get-grafico-dispositivos")
  .then((response) => response.json())
  .then((data) => {
    let mappedData = data.map(item => ({
        name: item.tipo,
        y: item.cantidad
    }));;
     

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container"
    );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: mappedData,
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));