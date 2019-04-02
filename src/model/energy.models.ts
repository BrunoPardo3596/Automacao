export interface GraphData {
  labels: string[];
  datasets: GraphInformation[];
}

export interface GraphInformation {
  label: string,
  fillColor: string,
  strokeColor: string,
  pointColor: string,
  pointStrokeColor: string,
  pointHighlightFill: string,
  pointHighlightStroke: string,
  data: number[],
  xAxisID: string,
}