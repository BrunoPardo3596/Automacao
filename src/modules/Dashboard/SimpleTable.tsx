import * as React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

export enum EquipmentType {
  Total = 'Total',
  iluminacao = 'Iluminação',
  rede = 'Rede',
  ar_cond = 'Ar Condicionado',
  bancadas = 'Bancadas',
  servidor = 'Servidor'
}

export interface ISimpleTableProps {
  data: any
}

class SimpleTable extends React.Component<ISimpleTableProps, any> {
  render() {
    return (
      <Paper>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Equipamento</TableCell>
              <TableCell align="right">Consumo (KWh)</TableCell>
              <TableCell align="right">Gasto (R$)</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {
              this.props.data ? this.props.data.map((n: any) => (
              <TableRow key={n.nome}>
                <TableCell component="th" scope="row">{EquipmentType[n.nome]}</TableCell>
                <TableCell align="right">{n.consumo}</TableCell>
                <TableCell align="right">{n.gasto}</TableCell>
              </TableRow>
              )): null
            }
          </TableBody>
        </Table>
      </Paper>
    );
  }
}

export default SimpleTable;