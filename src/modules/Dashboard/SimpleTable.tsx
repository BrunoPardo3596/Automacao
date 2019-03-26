import * as React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

let id = 0;
function createData(name: string, calories: number, fat: number, carbs: number, protein: number) {
  id += 1;
  return { id, name, calories, fat, carbs, protein };
}

const data = [
  createData('Geladeira', 159, 6.0, 24, 4.0),
  createData('Ar condicionado', 237, 9.0, 37, 4.3),
  createData('Televisão', 262, 16.0, 24, 6.0),
  createData('Chuveiro', 305, 3.7, 67, 4.3),
  createData('Luzes', 356, 16.0, 49, 3.9),
];

function SimpleTable() {

  return (
    <Paper>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Device</TableCell>
            <TableCell align="right">Teste</TableCell>
            <TableCell align="right">Potência</TableCell>
            <TableCell align="right">Consumo</TableCell>
            <TableCell align="right">Gasto</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map(n => (
            <TableRow key={n.id}>
              <TableCell component="th" scope="row">
                {n.name}
              </TableCell>
              <TableCell align="right">{n.calories}</TableCell>
              <TableCell align="right">{n.fat}</TableCell>
              <TableCell align="right">{n.carbs}</TableCell>
              <TableCell align="right">{n.protein}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
  );
}

export default SimpleTable;