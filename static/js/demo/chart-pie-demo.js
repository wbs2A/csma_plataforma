// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart1");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Lançamentos", "Atrasos", "Em andamento"],
    datasets: [{
      data: [55, 30, 15],
      backgroundColor: ['#7ddfb4', '#c80030', '#00cc72'],
      hoverBackgroundColor: ['#7ddfb4', '#c80030', '#00cc72'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});


var ctx1 = document.getElementById("myPieChart2");
var myPieChart1 = new Chart(ctx1, {
  type: 'bar',
  data: {
    labels: ["Chamados atendidos", "Em andamento", "Solicitações"],
    datasets: [{
      data: [66, 20, 19],
      backgroundColor: ['#4e73df', '#e6f253', '#cc967f'],
      hoverBackgroundColor: ['#3e5ab4', '#c2ce48', '#c18e77'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});

var ctx2 = document.getElementById("myPieChart3");
var myPieChart2 = new Chart(ctx2, {
  type: 'doughnut',
  data: {
    labels: ["Reuniões", "Parecer", "Em andamento"],
    datasets: [{
      data: [55, 30, 15],
      backgroundColor: ['#4cdfbe', '#9a53c8', '#cc554c'],
      hoverBackgroundColor: ['#4cdfbe', '#9a53c8', '#cc554c'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});

var ctx3 = document.getElementById("myPieChart4").getContext('2d');

//line
var myLineChart = new Chart(ctx3, {
    type: 'line',
    data: {
        labels: ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho"],
        datasets: [{
            label: "Feedback negativo",
            data: [65, 59, 80, 81, 56, 55, 40],
            backgroundColor: [
                'rgba(105, 0, 132, .2)',
            ],
            borderColor: [
                'rgba(200, 99, 132, .7)',
            ],
            borderWidth: 2
        },
            {
                label: "Feedback positivo",
                data: [28, 48, 40, 19, 86, 27, 90],
                backgroundColor: [
                    'rgba(0, 137, 132, .2)',
                ],
                borderColor: [
                    'rgba(0, 10, 130, .7)',
                ],
                borderWidth: 2
            }
        ]
    },
    options: {
        responsive: true
    }
});

/*var myPieChart3 = new Chart(ctx3, {
  type: 'bar',
  data: {
    labels: ["Inserções de mídia", "Feedback positivo", "Feedback negativo"],
    datasets: [{
      data: [38, 30, 8],
      backgroundColor: ['#9ddfd0', '#00cc72', '#eb6751'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
*/

var ctx4 = document.getElementById("myPieChart5");
var myPieChart4 = new Chart(ctx4, {
  type: 'bar',
  data: {
    labels: ["Direct", "Referral", "Social"],
    datasets: [{
      data: [55, 30, 15],
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});