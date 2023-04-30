<p>Recently, I have been dealing quite a bit with cryptography-related issues. Therefore, an idea arose to create a script that will generate a complex password. As in previous cases, I am creating a Docker image that I am using. However, if you want, I also share the script itself. Therefore, you can run it using Python installed on your local system. The script is located in the Github repository.</p><br />

<p><strong>Downloading files from Github:</strong></p>
<p><code>git clone https://github.com/kgodzisz/password-generator.git</code></p><br />

<p><strong>Creating your own image in your local repository:</strong></p>
<p><code>docker build -t password-generator .</code></p><br />

<p><strong>Running the tool:</strong></p>
<p><code>docker run --rm password-generator</code></p><br />

<p><strong>The second way is to download the prepared file from the Docker Hub repository:</strong></p>
<p><code>docker run --rm kgodzisz/password-generator</code></p><br />

<p><strong>Description of the options used in the commands:</strong></p>
<p><code>--rm</code> - the container will automatically be deleted after it is exited;</p> 
<p><code>password-generator</code> - the name of the created image that we want to use;</p>
<p><code>kgodzisz/password-generator</code> - the address to the image on the DockerHub platform.</p><br />

<p><strong>Blog</strong>: <a href="https://dockeryzacjaswiata.pl" target="blank">https://dockeryzacjaswiata.pl</a></p>
<p><strong>Docker Hub</strong>: <a href="https://hub.docker.com/r/kgodzisz/password-generator" target="_blank">https://hub.docker.com/r/kgodzisz/password-generator</p>
