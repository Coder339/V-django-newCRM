// import React from 'react';
// import { List, Avatar, Space } from 'antd';

import React, { Component } from 'react';

class Article extends Component {
  render() {
    return this.props.data.map((todo) => (
      <div>
         <p>{todo.first_name}</p>
      </div>
      
    ));
    
  }
}

export default Article;

// const Article = (props) => {
//     return (
//         <List
//         itemLayout="vertical"
//         size="large"
//         pagination={{
//           onChange: page => {
//             console.log(page);
//           },
//           pageSize: 3,
//         }}
//         dataSource={props.data}
//         footer={
//           <div>
//             <b>Customers</b>
//           </div>
//         }
//         renderItem={item => (
//           <List.Item
//             key={item.first_name}
//           >
//             <List.Item.Meta
//               avatar={<Avatar src={item.avatar} />}
//               title={<a href={item.href}>{item.first_name}</a>}
//               description={item.email_id}
          
//             />
            
//             {item.content}
//           </List.Item>
//         )}
//       />
//     );
// }



// export default Article;


