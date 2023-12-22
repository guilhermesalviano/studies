import React from 'react';
import  { CircularProgressbar } from 'react-circular-progressbar';
import { MdCheckCircle, MdError, MdLink } from 'react-icons/md';

import { Container, FileInfo, Preview } from './styles';

const FileList = ({ files }) => (
    <Container>
        {files.map(uploadedFile => {
            <li>
                <FileInfo>
                    <Preview src={uploadedFile.Preview} />
                    <div>
                        <strong>uploadedFile.name</strong>
                        <span>uploadedFile.readbleSize<button onClick={()=>{}}>Excluir</button></span>
                    </div>
                </FileInfo>

                <div>
                    {!uploadedFile.uploaded && !uploadedFile.error && (
                        <CircularProgressbar
                            styles={{
                                root: { width: 24},
                                path: { stroke: '#7159c1' }
                            }}
                            stokeWidth={10}
                            value={uploadedFile.progress}
                        />
                    )}

                    {uploadedFile.url && (
                        <a
                            href="http://localhost:3000/files/5c1b205c8f090fd9a2b06ad05aba4ff7-trist-eu.jpeg"
                            target="_blank"
                            rel="noopener noreferrer">
                            <MdLink style={{ marginRight: 8 }} size={24} color="#222" />
                        </a>
                    )}
                    { uploadedFile.uploaded && <MdCheckCircle size={24} color="#78e5d5" />}
                    { uploadedFile.error && <MdError size={24} color="#e57878" />}
                </div>
            </li>
        })}
    </Container>
);

export default FileList;
