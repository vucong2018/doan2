/* global Chart, coreui */

/**
 * --------------------------------------------------------------------------
 * CoreUI Boostrap Admin Template (v4.0.2): main.js
 * Licensed under MIT (https://coreui.io/license)
 * --------------------------------------------------------------------------
 */
// Disable the on-canvas tooltip
Chart.defaults.pointHitDetectionRadius = 1;
Chart.defaults.plugins.tooltip.enabled = false;
Chart.defaults.plugins.tooltip.mode = 'index';
Chart.defaults.plugins.tooltip.position = 'nearest';
Chart.defaults.plugins.tooltip.external = coreui.ChartJS.customTooltips;
Chart.defaults.defaultFontColor = '#646470';

const random = (min, max) => {
  // eslint-disable-next-line no-mixed-operators
  return Math.floor(Math.random() * (max - min + 1) + min);
}; // eslint-disable-next-line no-unused-vars

var getTempData = $.get('/data')
getTempData.done(function(results){
  // Humi
  var cardChart1 = new Chart(document.getElementById('card-chart1'), {
    type: 'line',
    data: {
      labels: results.time_list,
      datasets: [{
        label: 'Data of Humi',
        backgroundColor: 'transparent',
        borderColor: 'rgba(255,255,255,.55)',
        pointBackgroundColor: coreui.Utils.getStyle('--cui-primary'),
        data: results.humi_list
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false
        }
      },
      maintainAspectRatio: false,
      scales: {
        x: {
          grid: {
            display: false,
            drawBorder: false
          },
          ticks: {
            display: false
          }
        },
        y: {
          min: 10,
          max: 100,
          display: false,
          grid: {
            display: false
          },
          ticks: {
            display: false
          }
        }
      },
      elements: {
        line: {
          borderWidth: 1,
          tension: 0.4
        },
        point: {
          radius: 4,
          hitRadius: 10,
          hoverRadius: 4
        }
      }
    }
  });

  // Soil
  var cardChart2 = new Chart(document.getElementById('card-chart2'), {
    type: 'line',
    data: {
      labels: results.time_list,
      datasets: [{
        label: 'My First dataset',
        backgroundColor: 'transparent',
        borderColor: 'rgba(255,255,255,.55)',
        pointBackgroundColor: coreui.Utils.getStyle('--cui-info'),
        data: results.soil_list
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false
        }
      },
      maintainAspectRatio: false,
      scales: {
        x: {
          grid: {
            display: false,
            drawBorder: false
          },
          ticks: {
            display: false
          }
        },
        y: {
          min: -20,
          max: 1040,
          display: false,
          grid: {
            display: false
          },
          ticks: {
            display: false
          }
        }
      },
      elements: {
        line: {
          borderWidth: 1
        },
        point: {
          radius: 4,
          hitRadius: 10,
          hoverRadius: 4
        }
      }
    }
  }); // eslint-disable-next-line no-unused-vars

  // Light
  var cardChart3 = new Chart(document.getElementById('card-chart3'), {
    type: 'line',
    data: {
      labels: results.time_list,
      datasets: [{
        label: 'My First dataset',
        backgroundColor: 'transparent',
        borderColor: 'rgba(255,255,255,.55)',
        pointBackgroundColor: coreui.Utils.getStyle('--cui-yellow'),
        data: results.light_list
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false
        }
      },
      maintainAspectRatio: false,
      scales: {
        x: {
          grid: {
            display: false,
            drawBorder: false
          },
          ticks: {
            display: false
          }
        },
        y: {
          min: -5,
          max: 1028,
          display: false,
          grid: {
            display: false
          },
          ticks: {
            display: false
          }
        }
      },
      elements: {
        line: {
          borderWidth: 1
        },
        point: {
          radius: 4,
          hitRadius: 10,
          hoverRadius: 4
        }
      }
    }
  }); // eslint-disable-next-line no-unused-vars
  

  // Temp
  var cardChart4 = new Chart(document.getElementById('card-chart4'), {
    type: 'line',
    data: {
      labels: results.time_list,
      datasets: [{
        label: 'My First dataset',
        backgroundColor: 'transparent',
        borderColor: 'rgba(255,255,255,.55)',
        pointBackgroundColor: coreui.Utils.getStyle('--cui-red'),
        data: results.temp_list
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false
        }
      },
      maintainAspectRatio: false,
      scales: {
        x: {
          grid: {
            display: false,
            drawBorder: false
          },
          ticks: {
            display: false
          }
        },
        y: {
          min: -5,
          max: 55,
          display: false,
          grid: {
            display: false
          },
          ticks: {
            display: false
          }
        }
      },
      elements: {
        line: {
          borderWidth: 1
        },
        point: {
          radius: 4,
          hitRadius: 10,
          hoverRadius: 4
        }
      }
    }
  }); // eslint-disable-next-line no-unused-vars


  var mainChart = new Chart(document.getElementById('main-chart'), {
    type: 'line',
    data: {
      labels: results.time_list,
      datasets: [{
        label: 'My First dataset',
        backgroundColor: coreui.Utils.hexToRgba(coreui.Utils.getStyle('--cui-info'), 10),
        borderColor: coreui.Utils.getStyle('--cui-info'),
        pointHoverBackgroundColor: '#fff',
        borderWidth: 2,
        data: [random(50, 200), random(50, 200), random(50, 200), random(50, 200), random(50, 200), random(50, 200), random(50, 200)],
        fill: true
      }, {
        label: 'My Second dataset',
        borderColor: coreui.Utils.getStyle('--cui-success'),
        pointHoverBackgroundColor: '#fff',
        borderWidth: 2,
        data: [random(50, 200), random(50, 200), random(50, 200), random(50, 200), random(50, 200), random(50, 200), random(50, 200)]
      }, {
        label: 'My Third dataset',
        borderColor: coreui.Utils.getStyle('--cui-danger'),
        pointHoverBackgroundColor: '#fff',
        borderWidth: 1,
        borderDash: [8, 5],
        data: [100, 100, 100, 100, 100, 100, 100]
      }]
    },
    options: {
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        }
      },
      scales: {
        x: {
          grid: {
            drawOnChartArea: false
          }
        },
        y: {
          ticks: {
            beginAtZero: true,
            maxTicksLimit: 10,
            stepSize: Math.ceil(1100 / 5),
            max: 1023,
            min: 0
          }
        }
      },
      elements: {
        line: {
          tension: 0.4
        },
        point: {
          radius: 0,
          hitRadius: 10,
          hoverRadius: 4,
          hoverBorderWidth: 3
        }
      }
    }
  });
});
 






//# sourceMappingURL=main.js.map