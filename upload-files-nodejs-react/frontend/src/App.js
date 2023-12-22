import React from 'react';
import { uniqueId } from 'loadsh';
import filesize from 'filesize';

import GlobalStyle from './styles/global';
import { Container, Content } from './styles';

import Upload from './components/Upload';
import FileList from './components/FileList';

function App() {
  state = {
    uploadedFiles: [],
  };

  handleUpload = files => {
    console.log(files);
    const uploadedFiles = files.map(file => ({
      file,
      id: uniqueId(),
      name: file.name,
      readableSize: filesize(file.size),
      preview: URL.createObjectURL(file),
      progress: 0,
      uploaded: false,
      error: false,
      url: null,
    }))
  };

  setState({
    uploadedFiles: state.uploadedFiles.concat(uploadedFiles);
  })

  return (
    <Container>
      <GlobalStyle />
      <Content>
        <Upload onUpload={handleUpload} />
        {!!uploadedFiles.length && (
          <FileList files={uploadedFiles} />
        )}
      </Content>
    </Container>
    
    
  );
}

export default App;
