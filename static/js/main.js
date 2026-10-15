document.addEventListener("DOMContentLoaded", function () {


    // ------------------------------------------------
    // CHART DEFAULTS
    // ------------------------------------------------

    if (typeof Chart !== "undefined") {

        Chart.defaults.color = "#8996a8";

        Chart.defaults.borderColor =
            "rgba(255,255,255,0.06)";

        Chart.defaults.font.family =
            "Inter, system-ui, sans-serif";

    }


    // ------------------------------------------------
    // FAILURE DISTRIBUTION
    // ------------------------------------------------

    const failureCanvas =
        document.getElementById("failureChart");


    if (failureCanvas) {

        new Chart(failureCanvas, {

            type: "doughnut",

            data: {

                labels: [
                    "Normal",
                    "Failure"
                ],

                datasets: [{

                    data: [
                        9661,
                        339
                    ],

                    backgroundColor: [
                        "#5be7c4",
                        "#ff5f6d"
                    ],

                    borderWidth: 0

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                cutout: "72%",

                plugins: {

                    legend: {

                        position: "bottom",

                        labels: {
                            padding: 20
                        }

                    }

                }

            }

        });

    }



    // ------------------------------------------------
    // FAILURE RATE BY MACHINE TYPE
    // ------------------------------------------------

    const typeCanvas =
        document.getElementById("typeChart");


    if (typeCanvas) {

        new Chart(typeCanvas, {

            type: "bar",

            data: {

                labels: [
                    "Type L",
                    "Type M",
                    "Type H"
                ],

                datasets: [{

                    label: "Failure Rate (%)",

                    data: [
                        3.92,
                        2.77,
                        2.09
                    ],

                    backgroundColor:
                        "#5be7c4",

                    borderRadius: 7

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {
                        display: false
                    }

                },

                scales: {

                    y: {

                        beginAtZero: true,

                        title: {

                            display: true,

                            text: "Failure Rate (%)"

                        },

                        grid: {

                            color:
                                "rgba(255,255,255,0.05)"

                        }

                    },

                    x: {

                        grid: {
                            display: false
                        }

                    }

                }

            }

        });

    }



    // ------------------------------------------------
    // FEATURE IMPORTANCE
    // ------------------------------------------------

    const importanceCanvas =
        document.getElementById(
            "importanceChart"
        );


    if (importanceCanvas) {

        new Chart(
            importanceCanvas,
            {

                type: "bar",

                data: {

                    labels: [

                        "Mechanical Power",

                        "Wear × Torque",

                        "Rotational Speed",

                        "Torque",

                        "Temperature Difference",

                        "Tool Wear",

                        "Air Temperature",

                        "Process Temperature",

                        "Type L",

                        "Type M"

                    ],

                    datasets: [{

                        label:
                            "Feature Importance",

                        data: [

                            0.215346,

                            0.215306,

                            0.165991,

                            0.128057,

                            0.115621,

                            0.056086,

                            0.037699,

                            0.032766,

                            0.022734,

                            0.010393

                        ],

                        backgroundColor:
                            "#5be7c4",

                        borderRadius: 5

                    }]

                },


                options: {

                    indexAxis: "y",

                    responsive: true,

                    maintainAspectRatio: false,

                    plugins: {

                        legend: {
                            display: false
                        }

                    },

                    scales: {

                        x: {

                            beginAtZero: true,

                            grid: {

                                color:
                                    "rgba(255,255,255,0.05)"

                            }

                        },

                        y: {

                            grid: {
                                display: false
                            }

                        }

                    }

                }

            }
        );

    }

});