var issue_options = {
      		chart: {
      			type: "area",
      			fontFamily: 'inherit',
      			height: 192,
      			sparkline: {
      				enabled: true
      			},
      			animations: {
      				enabled: true
      			},
      		},
      		dataLabels: {
      			enabled: false,
      		},
      		fill: {
      			opacity: .16,
      			type: 'solid'
      		},
      		stroke: {
      			width: 2,
      			lineCap: "round",
      			curve: "smooth",
      		},
      		series: [{
      			name: "Issue",
      			data: issue_data.series
      		}],
      		grid: {
      			strokeDashArray: 4,
      		},
      		xaxis: {
      			labels: {
      				padding: 0,
      			},
      			tooltip: {
      				enabled: false
      			},
      			axisBorder: {
      				show: true,
      			},
      			type: 'datetime',
      		},
      		yaxis: {
      			labels: {
      				padding: 4
      			},
      		},
      		labels: issue_data.labels,
      		colors: ["#206bc4"],
      		legend: {
      			show: true,},
      		point: {
      			show: true
      		},
      	}

var clientele_options = {
    chart: {
    	type: "pie",
    	fontFamily: 'inherit',
    	animations: {
    		enabled: true
    	},
    },
    series: clientele_data.series,
    labels: clientele_data.labels,
}

var sign_options = {
    chart: {
    	type: "pie",
    	fontFamily: 'inherit',
    	animations: {
    		enabled: true
    	},
    },
    series: sign_data.series,
    labels: sign_data.labels,
    colors: ["#2fb344", "#d63939", "#038ffb", "#424242"]
}

var pov_options ={
          series: [{
          name: 'Frequency in percentage',
          data: pov_data.series
        }],
          chart: {
          type: 'bar',
          height: 350,
          toolbar: {
              show:false
          }
        },
        plotOptions: {
          bar: {
            borderRadius: 4,
            horizontal: true,
            distributed: true,
          }
        },
        dataLabels: {
          enabled: true,
          formatter: function (val, opts) {
            return val + '%'
            }
        },
        xaxis: {
          categories: pov_data.labels,
        },
        legend: {
            show: false,
        }
        };

var rating_summary_options = {
          series: [
              {
          name: 'Rating',
          data: rating_data.series,
        }
        ],
          chart: {
          type: 'bar',
          height: 350,
          toolbar: {
            show: false
          }
        },
        plotOptions: {
          bar: {
            borderRadius: 4,
            horizontal: true,
            distributed: true,
          }
        },
        dataLabels: {
          enabled: false,
        },
        xaxis: {
          categories: rating_data.labels,
        },
        colors: rating_data.colors,
        };

var issue_summary_chart = new ApexCharts(document.querySelector("#issue_summary"), issue_options).render();
var clientele_summary_chart = new ApexCharts(document.querySelector("#clientele_summary"), clientele_options).render();
var sign_summary_chart = new ApexCharts(document.querySelector("#sign_summary"), sign_options).render();
var pov_summary_chart = new ApexCharts(document.querySelector("#pov_summary"), pov_options).render();
var rating_summary_chart = new ApexCharts(document.querySelector("#rating_summary"), rating_summary_options).render();