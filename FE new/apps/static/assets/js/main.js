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
var cardChart1, cardChart2,cardChart3, cardChart4, mainChart;
var getTempData = $.get('/data')
getTempData.done(function(results){
  humi_change = results.humi_list[6] / results.humi_list[5] - 1.0
  console.log(Math.round(humi_change*100)/100)
  $(".humi_value").text(results.humi_list[6] + "%");
  $(".soil_value").text(results.soil_list[6] + " Points");
  $(".light_value").text(results.light_list[6] + " Points");
  $(".temp_value").text(results.temp_list[6]);
  // Humi
    type = 'line'
    data_1 = {
      labels: results.time_list,
      datasets: [{
        label: 'Data of Humi',
        backgroundColor: 'transparent',
        borderColor: 'rgba(255,255,255,.55)',
        pointBackgroundColor: coreui.Utils.getStyle('--cui-primary'),
        data: results.humi_list
      }]
    }
    options_1 = {
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
    cardChart1 = new Chart(document.getElementById('card-chart1'), {type : type, data : data_1,options : options_1})
  //   cardChart1 = new Chart(document.getElementById('card-chart1'), {
  //   type: 'line',
  //   data: {
  //     labels: results.time_list,
  //     datasets: [{
  //       label: 'Data of Humi',
  //       backgroundColor: 'transparent',
  //       borderColor: 'rgba(255,255,255,.55)',
  //       pointBackgroundColor: coreui.Utils.getStyle('--cui-primary'),
  //       data: results.humi_list
  //     }]
  //   },
  //   options: {
  //     plugins: {
  //       legend: {
  //         display: false
  //       }
  //     },
  //     maintainAspectRatio: false,
  //     scales: {
  //       x: {
  //         grid: {
  //           display: false,
  //           drawBorder: false
  //         },
  //         ticks: {
  //           display: false
  //         }
  //       },
  //       y: {
  //         min: 10,
  //         max: 100,
  //         display: false,
  //         grid: {
  //           display: false
  //         },
  //         ticks: {
  //           display: false
  //         }
  //       }
  //     },
  //     elements: {
  //       line: {
  //         borderWidth: 1,
  //         tension: 0.4
  //       },
  //       point: {
  //         radius: 4,
  //         hitRadius: 10,
  //         hoverRadius: 4
  //       }
  //     }
  //   }
  // });

  // Soil
    cardChart2 = new Chart(document.getElementById('card-chart2'), {
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
    cardChart3 = new Chart(document.getElementById('card-chart3'), {
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
    cardChart4 = new Chart(document.getElementById('card-chart4'), {
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


    mainChart = new Chart(document.getElementById('main-chart'), {
    type: 'line',
    data: {
      labels: results.time_list,
      datasets: [{
        label: 'My First dataset',
        backgroundColor: coreui.Utils.hexToRgba(coreui.Utils.getStyle('--cui-info'), 10),
        borderColor: coreui.Utils.getStyle('--cui-info'),
        pointHoverBackgroundColor: '#fff',
        borderWidth: 2,
        data: results.humi_list,
        fill: true
      }, {
        label: 'My Second dataset',
        borderColor: coreui.Utils.getStyle('--cui-success'),
        pointHoverBackgroundColor: '#fff',
        borderWidth: 2,
        data: results.temp_list
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
 
function updateChart() {
  var getUpadte = $.get('/data')
  
  getUpadte.done(function(results){
    $(".humi_value").text(results.humi_list[6] + "%");
    $(".soil_value").text(results.soil_list[6] + " Points");
    $(".light_value").text(results.light_list[6] + " Points");
    $(".temp_value").text(results.temp_list[6]);
    cardChart1.data.datasets.pop()
    cardChart2.data.datasets.pop()
    cardChart3.data.datasets.pop()
    cardChart4.data.datasets.pop()
    cardChart1.data.datasets.push({
      label: 'Data of Humi',
        backgroundColor: 'transparent',
        borderColor: 'rgba(255,255,255,.55)',
        pointBackgroundColor: coreui.Utils.getStyle('--cui-primary'),
        data: results.humi_list
    })
    cardChart2.data.datasets.push({
      label: 'Data of Soil',
        backgroundColor: 'transparent',
        borderColor: 'rgba(255,255,255,.55)',
        pointBackgroundColor: coreui.Utils.getStyle('--cui-info'),
        data: results.soil_list
    })
    cardChart3.data.datasets.push({
      label: 'Data of Light',
        backgroundColor: 'transparent',
        borderColor: 'rgba(255,255,255,.55)',
        pointBackgroundColor: coreui.Utils.getStyle('--cui-yellow'),
        data: results.light_list
    })
    cardChart4.data.datasets.push({
      label: 'My First dataset',
        backgroundColor: 'transparent',
        borderColor: 'rgba(255,255,255,.55)',
        pointBackgroundColor: coreui.Utils.getStyle('--cui-red'),
        data: results.temp_list
    })
    cardChart1.update()
    cardChart2.update()
    cardChart3.update()
    cardChart4.update()
      
    
  })

  
  
}
$("#refresh").on('click', updateChart)





//# sourceMappingURL=main.js.map