import { withTheme, WithTheme } from '@material-ui/core';
import * as React from 'react';

export enum BoxSize {
  Small = 1,
  Medium = 2,
  Large = 3,
  XLarge = 4
}

interface IBoxBase extends WithTheme {
  size?: BoxSize;
  children: React.ReactNode;
}

const BoxBase: React.FunctionComponent<IBoxBase> = ({ theme, children, size = BoxSize.Medium }: IBoxBase) => (
  <div style={{ padding: theme.spacing.unit * size }} >
    {children}
  </div>
)

const Box = withTheme()(BoxBase);

export default Box;
