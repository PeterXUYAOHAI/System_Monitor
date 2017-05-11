var gaugeOptions = {

    chart: {
        type: 'solidgauge'
    },

    title: null,

    pane: {
        center: ['50%', '85%'],
        size: '140%',
        startAngle: -90,
        endAngle: 90,
        background: {
            backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || '#EEE',
            innerRadius: '60%',
            outerRadius: '100%',
            shape: 'arc'
        }
    },

    tooltip: {
        enabled: false
    },

    // the value axis
    yAxis: {
        stops: [
            [0.1, '#55BF3B'], // green
            [0.5, '#DDDF0D'], // yellow
            [0.9, '#DF5353'] // red
        ],
        lineWidth: 0,
        minorTickInterval: null,
        tickAmount: 2,
        title: {
            y: -70
        },
        labels: {
            y: 16
        }
    },

    plotOptions: {
        solidgauge: {
            dataLabels: {
                y: 5,
                borderWidth: 0,
                useHTML: true
            }
        }
    }
};


// The RPM gauge
var chartRpm = Highcharts.chart('container-rpm', Highcharts.merge(gaugeOptions, {
    yAxis: {
        min: 0,
        max: 100,
        title: {
            text: 'Memory Usage'
        }
    },

    series: [{
        name: 'Memory Usage',
        data: [1],
        dataLabels: {
            format: '<div style="text-align:center"><span style="font-size:25px;color:' +
                ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y:.1f}</span><br/>' +
                   '<span style="font-size:12px;color:silver">%</span></div>'
        },
        tooltip: {
            valueSuffix: ' revolutions/min'
        }
    }]

}));


setInterval(function () {
    // Speed
    var point,
        newVal,
        inc;

    if (chartRpm) {
        point = chartRpm.series[0].points[0];
        var newVal;
        $.ajax({url: "/ram_status", success: function(result){
        point.update(parseFloat(result));
    }});

     $.ajax({url: "/cpu_status", success: function(result){
        result = result.split(" ");
        for (i = 1; i <= parseInt(result[0]); i++) {
          document.getElementById('cpu_'+i).style.width= result[i] + '%';
          document.getElementById("cpu_"+i+"_p").innerHTML = result[i] + '%';
        }

    }});

    }
}, 500);
