import { GraphData } from "src/model/energy.models";
import {  Service } from 'typedi';

const data: GraphData = {
  labels: ["January", "February", "March", 
    "April", "May", "June", "July", 
    "August", "September", "October", "November", "Dezember"],
  datasets: [
    {
      label: "2018",
      fillColor: "rgba(220,220,220,0.2)",
      strokeColor: "rgba(220,220,220,1)",
      pointColor: "rgba(220,220,220,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(220,220,220,1)",
      data: [65, 59, 80, 81, 56, 55, 40, 20, 100, 200, 300, 350]
    },
    {
      label: "2019",
      fillColor: "rgba(151,187,205,0.2)",
      strokeColor: "rgba(151,187,205,1)",
      pointColor: "rgba(151,187,205,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(151,187,205,1)",
      data: [28, 48, 40, 19, 86, 27, 90, 30, 100, 200, 300, 350]
    }
  ]
};

@Service()
export class EnergyDataSource {
  getData(): GraphData {
    return data
  }
}
