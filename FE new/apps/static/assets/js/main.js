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
var getTempData = $.get('/data');

function checkdata(data, tag1, tag2, now_value, min_value, max_value)
{
  var percent = Math.round(((now_value - min_value) / (max_value - min_value)) * 100) + "%";
  if (data > 0)
  {
    data = "+" + data;
    $(tag1 + " ~ svg")[0].classList.remove("hide-icon");
    $(tag1 + " ~ svg")[1].classList.add("hide-icon");
  }
  else if (data < 0)
  {
    $(tag1 + " ~ svg")[1].classList.remove("hide-icon");
    $(tag1 + " ~ svg")[0].classList.add("hide-icon");
  }
  $(tag1).text(data + "%");
  $(tag2).css("width", percent);
}

$.get('/device').done(function(results) {
  $(".data_btn").each(function(index) {
    if (results.device_state[index] == 1) {$(this).prop('checked', 'true');}
  });
})

$(".data_btn").click(function() {
  d_id = $(this)[0].name
  d_state = ($(this).is(':checked') == true) ? 1 : 0
  const request1 = new XMLHttpRequest()
  request1.open('POST', `/device-change/${d_id}`)
  request1.send()
  
  dcs = (d_state == 1) ? 'OFF TO ON' : 'ON TO OFF'
  data_log = {device_id: d_id, human: 'Bao', descript: dcs};
  const request2 = new XMLHttpRequest()
  request2.open('POST', `/log/${JSON.stringify(data_log)}`)
  request2.send()
})

getTempData.done(function(results){
  var humi_change = Math.round(((results.humi_list[6] / results.humi_list[5]) - 1.0) * 10000) / 100;
  var soil_change = Math.round(((results.soil_list[6] / results.soil_list[5]) - 1.0) * 10000) / 100;
  var light_change = Math.round(((results.light_list[6] / results.light_list[5]) - 1.0) * 10000) / 100;
  var temp_change = Math.round(((results.temp_list[6] / results.temp_list[5]) - 1.0) * 10000) / 100;
  checkdata(humi_change, ".humi_chan", ".humi_bar", results.humi_list[6], 20, 90);
  checkdata(soil_change, ".soil_chan", ".soil_bar", results.soil_list[6], 0, 1023);
  checkdata(light_change, ".light_chan", ".light_bar", results.light_list[6], 0, 1023);
  checkdata(temp_change, ".temp_chan", ".temp_bar", results.temp_list[6], 0, 50);
  $(".humi_value").text(results.humi_list[6] + "%");
  $(".soil_value").text(results.soil_list[6] + " Pts");
  $(".light_value").text(results.light_list[6] + " Pts");
  $(".temp_value").text(results.temp_list[6]);
  // Humi
    type = 'line';
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
          // tension: 0.4
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
        label: 'Data of Soil',
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
        label: 'Data of Light',
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
        label: 'Data of Temp',
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
    type: 'bar',
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
    var humi_change = Math.round(((results.humi_list[6] / results.humi_list[5]) - 1.0) * 10000) / 100;
    var soil_change = Math.round(((results.soil_list[6] / results.soil_list[5]) - 1.0) * 10000) / 100;
    var light_change = Math.round(((results.light_list[6] / results.light_list[5]) - 1.0) * 10000) / 100;
    var temp_change = Math.round(((results.temp_list[6] / results.temp_list[5]) - 1.0) * 10000) / 100;
    checkdata(humi_change, ".humi_chan", ".humi_bar", results.humi_list[6], 20, 90);
    checkdata(soil_change, ".soil_chan", ".soil_bar", results.soil_list[6], 0, 1023);
    checkdata(light_change, ".light_chan", ".light_bar", results.light_list[6], 0, 1023);
    checkdata(temp_change, ".temp_chan", ".temp_bar", results.temp_list[6], 0, 50);
    $(".humi_value").text(results.humi_list[6] + "%");
    $(".soil_value").text(results.soil_list[6] + " Pts");
    $(".light_value").text(results.light_list[6] + " Pts");
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
      label: 'Data of Temp',
        backgroundColor: 'transparent',
        borderColor: 'rgba(255,255,255,.55)',
        pointBackgroundColor: coreui.Utils.getStyle('--cui-red'),
        data: results.temp_list
    })
    cardChart1.data.labels = results.time_list
    cardChart2.data.labels = results.time_list
    cardChart3.data.labels = results.time_list
    cardChart4.data.labels = results.time_list
    mainChart.data.labels = results.time_list
    mainChart.data.datasets =[{
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
    
    cardChart1.update()
    cardChart2.update()
    cardChart3.update()
    cardChart4.update()
    mainChart.update()
      
    
  })

  
  
}
$("#refresh").on('click', updateChart)





//# sourceMappingURL=main.js.map