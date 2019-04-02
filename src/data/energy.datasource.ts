import { GraphData } from "src/model/energy.models";
import {  Service } from 'typedi';
import axios from 'axios';

const data: GraphData = {
  labels: ["January", "February", "March", 
    "April", "May", "June", "July", 
    "August", "September", "October", "November", "Dezember"],
  datasets: [
    {
      label: "2019",
      fillColor: "rgba(220,220,220,0.2)",
      strokeColor: "rgba(220,220,220,1)",
      pointColor: "rgba(220,220,220,1)",
      pointStrokeColor: "#fff",
      pointHighlightFill: "#fff",
      pointHighlightStroke: "rgba(220,220,220,1)",
      xAxisID: 'Months',
      data: [65, 59, 80, 81, 56, 55, 40, 20, 100, 200, 300, 350]
    },
  ]
};

const baseUrl = "127.0.0.1:5000";

// const tarifa: number = 0.4836;

@Service()
export class EnergyDataSource {
  getData(): GraphData {
    // return data

    axios.get(`${baseUrl}`, {headers: {Authorization: localStorage.getItem("token")}})
      .then(response => {
        console.log(response.data.pagination.total);
      });
    return data;
  }
}
