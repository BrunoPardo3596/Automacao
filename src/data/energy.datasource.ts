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

const baseUrl = "http://127.0.0.1:5000";

// const tarifa: number = 0.4836;

@Service()
export class EnergyDataSource {
  async getAnualMonthByMonth(): Promise<GraphData> {

    return axios.get(`${baseUrl}/consumoAnualDet`)
      .then(response => {
        return this.getAnualData(response.data.labSoft);
      }).catch(err => {
        console.log(err);
        return data;
      });
  }

  async getMonthlyConsume(): Promise<any> {
    return axios.get(`${baseUrl}/consumoMensal`)
      .then(response => {
        return response.data.labSoft
      }).catch(err => {
        console.log(err);
        return null;
      });
  }

  async getAnualConsume(): Promise<any> {
    return axios.get(`${baseUrl}/consumoAnual`)
      .then(response => {
        return response.data.labSoft
      }).catch(err => {
        console.log(err);
        return null;
      });
  }

  async getMonthlyWasteDayByDay(): Promise<any> {
    return axios.get(`${baseUrl}/consumoMensalDet`)
      .then((response) => {
        console.log(response.data.labSoft)
        return this.getMonthData(response.data.labSoft)//this.getMonthData(response.data.labSoft);
      }).catch(err => {
        console.log(err);
        return null;
      });
  }

  private getMonthData = (data: any) => {
    return {
      labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
        "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"
      ],
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
          data: [data[0].dados[0].gasto, data[1].dados[0].gasto, data[2].dados[0].gasto, data[3].dados[0].gasto,
            data[4].dados[0].gasto, data[5].dados[0].gasto, data[6].dados[0].gasto, data[7].dados[0].gasto, data[8].dados[0].gasto, 
            data[9] ? data[9].dados[0].gasto: 0,
            data[10] ? data[10].dados[0].gasto: 0,
            data[11] ? data[11].dados[0].gasto: 0,
            data[12] ? data[12].dados[0].gasto: 0,
            data[13] ? data[13].dados[0].gasto: 0,
            data[14] ? data[14].dados[0].gasto: 0,
            data[15] ? data[15].dados[0].gasto: 0,
            data[16] ? data[16].dados[0].gasto: 0,
            data[17] ? data[17].dados[0].gasto: 0,
            data[18] ? data[18].dados[0].gasto: 0, 
            data[19] ? data[19].dados[0].gasto: 0,
            data[20] ? data[20].dados[0].gasto: 0, 
            data[21] ? data[21].dados[0].gasto: 0, 
            data[22] ? data[22].dados[0].gasto: 0, 
            data[23] ? data[23].dados[0].gasto: 0, 
            data[24] ? data[24].dados[0].gasto: 0, 
            data[25] ? data[25].dados[0].gasto: 0, 
            data[26] ? data[26].dados[0].gasto: 0, 
            data[27] ? data[27].dados[0].gasto: 0, 
            data[28] ? data[28].dados[0].gasto: 0, 
            data[29] ? data[29].dados[0].gasto: 0,
          ]
        },
      ]
    }
  }

  private getAnualData = (data: any) => {
    return {
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
          data: [0, 
          data[0].dados[0].gasto, 
          data[1].dados[0].gasto, 
          data[2].dados[0].gasto, 
          data[3] ? data[3].dados[0].gasto: 0, 
          data[4] ? data[4].dados[0].gasto: 0, 
          data[5] ? data[5].dados[0].gasto: 0, 
          data[6] ? data[6].dados[0].gasto: 0, 
          data[7] ? data[7].dados[0].gasto: 0, 
          data[8] ? data[8].dados[0].gasto: 0, 
          data[9] ? data[9].dados[0].gasto: 0, ]
        },
      ]
    }
  }
}
