import * as React from 'react';
import './Login/Login.css'

const errorMessage = (props: any) => {
  let content = null;
  if(props.isValid){
    content = (
      <p className="text-danger">{props.content}</p>
    )
  }
  return(
    content
  );
}

export default errorMessage